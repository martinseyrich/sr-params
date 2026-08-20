# Parameter Repository

This repository holds the source-of-truth YAML parameter files for insertion
devices (undulators, wigglers, etc.) and storage rings, together with the two
Python scripts used to combine them into single, machine-generated summary
files.

## Repository layout

```
.
├── combine_ids.py     # Combines all insertion-device source files
├── combine_srs.py      # Combines all storage-ring source files
├── IDs/                 # Source YAML files for insertion devices (subfolders allowed)
│   └── ...
└── SRs/                  # Source YAML files for storage rings (subfolders allowed)
    └── ...
```

You are free to organize the `IDs/` and `SRs/` folders into as many
subdirectories as you like (e.g. by beamline, by ring, by year) — both
scripts crawl recursively and pick up every compatible `.yaml`/`.yml` file
they find.

## Editing source data

- **Never edit a generated output file by hand.** Both scripts stamp their
  output with a "machine generated" header — edit the source files under
  `IDs/` or `SRs/` instead, then regenerate.
- Each source file must have `IDs:` or `SRs:` (respectively) as its
  top-level key, containing a list of entries. Files without this root key,
  or without a `.yaml`/`.yml` extension, are ignored by the scripts.
- Every entry needs a unique `name` field and a `date` field. If the same
  `name` shows up in more than one source file, the entry with the newest
  `date` wins; if `name` and `date` are both identical, the script prints a
  warning and keeps the first one it finds.

## Generating the combined files

Insertion devices:
```
python combine_ids.py IDs combined_ids.yaml
```

Storage rings:
```
python combine_srs.py SRs combined_srs.yaml
```

Both commands print a summary line and any warnings (duplicate/clashing
entries, malformed files, missing fields, etc.) to the console — check this
output after every run.

### What each script does

**`combine_ids.py`**
- Combines all insertion-device entries under `IDs/`.
- Sorts the output: `PETRA PBxx` entries first (ascending by number, then by
  any letter suffix like `PB31a`/`PB31b`), then `PETRA Pxx` entries the same
  way, then everything else alphanumerically.

**`combine_srs.py`**
- Combines all storage-ring entries under `SRs/`.
- Calculates `emittance_hor` / `emittance_ver` (in pm·rad) from each entry's
  beam size (µm) and divergence (µrad).
- Calculates `phase_space_density` as `current / (emittance_hor ×
  emittance_ver)`.
- Sorts the output by `phase_space_density`, highest first.

## Requirements

- Python 3
- [PyYAML](https://pypi.org/project/PyYAML/) (`pip install pyyaml`)

## Authorship disclosure

The `combine_ids.py` and `combine_srs.py` scripts were written by Claude
(Anthropic). Unless a YAML entry explicitly states otherwise (e.g. in its
own `comment` field), all YAML data entries in `IDs/` and `SRs/` were
created by a human contributor, not by Claude.