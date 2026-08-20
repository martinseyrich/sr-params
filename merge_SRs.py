#!/usr/bin/env python3
"""
Crawl a directory tree (e.g. a folder called "SRs") for YAML storage-ring
parameter files and combine them into a single YAML file.

Rules:
- Only files ending in .yaml or .yml are considered; everything else is
  ignored.
- A YAML file is only used if its parsed top-level content is a mapping
  containing an "SRs" key (i.e. "SRs" is the document root). Files without
  this root key are ignored.
- Entries are matched by their "name" field. If two entries share the same
  name, the "date" field is inspected and only the entry with the newer date
  is kept.
- If both "name" and "date" are identical between two entries, a warning is
  printed and the first-encountered entry is kept.
- File traversal order is sorted (stable/reproducible), so ties resolve the
  same way on every run.
- For every entry, the horizontal and vertical emittance are calculated from
  the beam size and divergence (emittance = beamsize * divergence, assuming
  a beam waist with no dispersion/correlation contribution) and stored as
  "emittance_hor" / "emittance_ver" in pm*rad (beamsize in um * divergence
  in urad = pm*rad). The phase space density is then calculated as
  "current / (emittance_hor * emittance_ver)" and stored as
  "phase_space_density".
- The output entries are sorted by phase_space_density, highest first.

Usage:
    python combine_srs.py <input_dir> <output_file.yaml>
"""

import argparse
import sys
from datetime import date, datetime
from pathlib import Path

import yaml


def parse_date(value):
    """Normalize a date field into a `datetime.date` for comparison.

    PyYAML auto-parses unquoted ISO dates (YYYY-MM-DD) into `datetime.date`
    objects already. This also copes with the date being given as a plain
    (possibly quoted) string, or being missing entirely.
    """
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, str):
        for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
            try:
                return datetime.strptime(value.strip(), fmt).date()
            except ValueError:
                continue
    return None


def find_yaml_files(root: Path):
    """Recursively find all .yaml/.yml files under root, in stable sorted order."""
    files = [
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in (".yaml", ".yml")
    ]
    return sorted(files)


def load_srs_from_file(path: Path):
    """Load a YAML file and return its list of SR entries, or None if not applicable."""
    try:
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"WARNING: skipping '{path}' - could not parse YAML ({e})", file=sys.stderr)
        return None
    except OSError as e:
        print(f"WARNING: skipping '{path}' - could not read file ({e})", file=sys.stderr)
        return None

    if not isinstance(data, dict) or "SRs" not in data:
        # Root key isn't "SRs" -> not one of our parameter files, ignore silently
        return None

    srs = data["SRs"]
    if not isinstance(srs, list):
        print(f"WARNING: skipping '{path}' - 'SRs' key is not a list", file=sys.stderr)
        return None

    return srs


def add_emittances(entry, path):
    """Compute and attach emittance_hor / emittance_ver to an entry, in place.

    emittance [pm*rad] = beamsize [um] * divergence [urad]
    """
    name = entry.get("name", "<unnamed>")

    pairs = [
        ("hor", "beamsize_hor", "divergence_hor", "emittance_hor"),
        ("ver", "beamsize_ver", "divergence_ver", "emittance_ver"),
    ]

    for _, size_key, div_key, emit_key in pairs:
        size = entry.get(size_key)
        div = entry.get(div_key)

        if not isinstance(size, (int, float)) or not isinstance(div, (int, float)):
            print(
                f"WARNING: entry '{name}' in '{path}' is missing/has invalid "
                f"'{size_key}' or '{div_key}'; skipping emittance calculation "
                f"for '{emit_key}'.",
                file=sys.stderr,
            )
            continue

        entry[emit_key] = size * div


def add_phase_space_density(entry, path):
    """Compute and attach phase_space_density to an entry, in place.

    phase_space_density = current / (emittance_hor * emittance_ver)
    """
    name = entry.get("name", "<unnamed>")

    current = entry.get("current")
    emit_hor = entry.get("emittance_hor")
    emit_ver = entry.get("emittance_ver")

    if not isinstance(current, (int, float)):
        print(
            f"WARNING: entry '{name}' in '{path}' is missing/has invalid 'current'; "
            f"skipping phase_space_density calculation.",
            file=sys.stderr,
        )
        return

    if not isinstance(emit_hor, (int, float)) or not isinstance(emit_ver, (int, float)):
        print(
            f"WARNING: entry '{name}' in '{path}' is missing a computed emittance; "
            f"skipping phase_space_density calculation.",
            file=sys.stderr,
        )
        return

    if emit_hor == 0 or emit_ver == 0:
        print(
            f"WARNING: entry '{name}' in '{path}' has a zero emittance; "
            f"skipping phase_space_density calculation (division by zero).",
            file=sys.stderr,
        )
        return

    entry["phase_space_density"] = current / (emit_hor * emit_ver)


def combine(root: Path):
    combined = {}       # name -> entry dict
    combined_meta = {}  # name -> (date_or_None, source_path)

    for path in find_yaml_files(root):
        srs = load_srs_from_file(path)
        if not srs:
            continue

        for entry in srs:
            if not isinstance(entry, dict) or "name" not in entry:
                print(f"WARNING: skipping malformed entry (missing 'name') in '{path}'", file=sys.stderr)
                continue

            name = entry["name"]
            entry_date = parse_date(entry.get("date"))

            if name not in combined:
                combined[name] = entry
                combined_meta[name] = (entry_date, path)
                continue

            existing_date, existing_path = combined_meta[name]

            if entry_date is None or existing_date is None:
                print(
                    f"WARNING: duplicate name '{name}' found in '{existing_path}' and "
                    f"'{path}' but at least one entry has a missing/unparseable date; "
                    f"keeping the entry from '{existing_path}'.",
                    file=sys.stderr,
                )
                continue

            if entry_date == existing_date:
                print(
                    f"WARNING: duplicate entry for name '{name}' with identical date "
                    f"'{entry_date}' found in both '{existing_path}' and '{path}'. "
                    f"Keeping the entry from '{existing_path}'.",
                    file=sys.stderr,
                )
                continue

            if entry_date > existing_date:
                combined[name] = entry
                combined_meta[name] = (entry_date, path)
            # else: existing entry is newer -> keep it, discard this one

    entries = list(combined.values())
    for name, entry in combined.items():
        add_emittances(entry, combined_meta[name][1])
        add_phase_space_density(entry, combined_meta[name][1])

    return entries


def phase_space_density_sort_key(entry):
    """Sort key for descending order by phase space density (ascending sort,
    no reverse needed). Entries missing a computable value are always sorted
    to the end."""
    value = entry.get("phase_space_density")
    if not isinstance(value, (int, float)):
        return (1, 0.0, str(entry.get("name", "")))
    return (0, -value, str(entry.get("name", "")))


def main():
    parser = argparse.ArgumentParser(
        description="Crawl a directory of YAML storage-ring parameter files (rooted "
                    "under an 'SRs' key) and combine them into a single YAML file, "
                    "resolving name clashes by keeping the entry with the newest "
                    "'date', computing emittances, and sorting by horizontal emittance."
    )
    parser.add_argument("input_dir", type=Path, help="Root directory to crawl (e.g. 'SRs')")
    parser.add_argument("output_file", type=Path, help="Path to write the combined YAML file to")
    args = parser.parse_args()

    if not args.input_dir.is_dir():
        print(f"ERROR: '{args.input_dir}' is not a directory", file=sys.stderr)
        sys.exit(1)

    entries = combine(args.input_dir)
    entries.sort(key=phase_space_density_sort_key)

    output_data = {"SRs": entries}

    header = (
        "### =========================================================================\n"
        "### THIS FILE IS MACHINE GENERATED - DO NOT EDIT IT BY HAND.\n"
        "###\n"
        "### Any manual changes made here will be silently overwritten the next time\n"
        "### this file is regenerated. To change the data, edit the individual source\n"
        "### files instead (the per-ring YAML files under the 'SRs' directory tree),\n"
        "### then regenerate this file.\n"
        "###\n"
        "### Horizontal/vertical emittance (emittance_hor / emittance_ver, in pm*rad)\n"
        "### are calculated automatically from beamsize_hor/ver [um] and\n"
        "### divergence_hor/ver [urad], and phase_space_density (in mA/(pm*rad)^2)\n"
        "### is calculated automatically as current / (emittance_hor * emittance_ver).\n"
        "### Do not add these fields in the source files, they will be overwritten.\n"
        "### Entries are sorted by phase_space_density descending (highest first).\n"
        "###\n"
        "### HOW TO REGENERATE THIS FILE\n"
        "###   1. Edit or add the relevant source YAML file(s) under the 'SRs'\n"
        "###      directory (subdirectories are searched too). Each source file must\n"
        "###      have 'SRs:' as its top-level key and a 'date:' field on every\n"
        "###      entry, since the newest 'date' wins if the same 'name' appears in\n"
        "###      more than one source file.\n"
        "###   2. Run the generator script from the command line:\n"
        f"###        python combine_srs.py {args.input_dir} {args.output_file}\n"
        "###   3. Check the script's console output for warnings (e.g. duplicate\n"
        "###      name+date clashes, or missing beamsize/divergence values) and\n"
        "###      resolve them in the source files if needed.\n"
        "### =========================================================================\n\n"
    )

    with args.output_file.open("w", encoding="utf-8") as f:
        f.write(header)
        yaml.safe_dump(output_data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

    print(f"Combined {len(entries)} unique entries into '{args.output_file}'.")


if __name__ == "__main__":
    main()