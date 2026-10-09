### =========================================================================
### THIS FILE IS MACHINE GENERATED - DO NOT EDIT IT BY HAND.
###
### Any manual changes made here will be silently overwritten the next time
### this file is regenerated. To change the data, edit the individual source
### files instead (the per-ring YAML files under the 'SRs' directory tree),
### then regenerate this file.
###
### Horizontal/vertical emittance (emittance_hor / emittance_ver, in pm*rad)
### are calculated automatically from beamsize_hor/ver [um] and
### divergence_hor/ver [urad], and phase_space_density (in mA/(pm*rad)^2)
### is calculated automatically as current / (emittance_hor * emittance_ver).
### Do not add these fields in the source files, they will be overwritten.
### Entries are sorted by phase_space_density descending (highest first).
###
### HOW TO REGENERATE THIS FILE
###   1. Edit or add the relevant source YAML file(s) under the 'SRs'
###      directory (subdirectories are searched too). Each source file must
###      have 'SRs:' as its top-level key and a 'date:' field on every
###      entry, since the newest 'date' wins if the same 'name' appears in
###      more than one source file.
###   2. Run the generator script from the command line:
###        python combine_srs.py SRs merge_SRs.py
###   3. Check the script's console output for warnings (e.g. duplicate
###      name+date clashes, or missing beamsize/divergence values) and
###      resolve them in the source files if needed.
### =========================================================================

SRs:
- name: PETRA IV BM 5m
  energy: 6.0
  energy_spread: 0.1
  current: 200
  beamsize_hor: 5.1
  beamsize_ver: 5.1
  divergence_hor: 2.3
  divergence_ver: 2.3
  date: 2026-10-09
  reference1: PETRA IV EDR, P. 46 and P. 68, draft version Nov 17 2025
  reference2: ''
  reference3: ''
  comment: PETRA IV Brilliance Mode, fully-coupled, in 5m straight sections (4.3m
    usable ID length)
  emittance_hor: 11.729999999999999
  emittance_ver: 11.729999999999999
  phase_space_density: 1.4535633742729461
- name: PETRA IV BM 10m
  energy: 6.0
  energy_spread: 0.1
  current: 200
  beamsize_hor: 6.9
  beamsize_ver: 6.9
  divergence_hor: 1.7
  divergence_ver: 1.7
  date: 2026-10-09
  reference1: PETRA IV EDR, P. 46 and P. 68, draft version Nov 17 2025
  reference2: ''
  reference3: ''
  comment: PETRA IV Brilliance Mode, fully-coupled, in 10m (?) long straight sections
  emittance_hor: 11.73
  emittance_ver: 11.73
  phase_space_density: 1.4535633742729457
- name: APS-U BM
  energy: 6.0
  energy_spread: 0.1
  current: 200
  beamsize_hor: 14.7
  beamsize_ver: 3.2
  divergence_hor: 2.8
  divergence_ver: 1.3
  date: '2026-07-29'
  reference1: https://www.aps.anl.gov/sites/www.aps.anl.gov/files/APS-Uploads/Aps-Upgrade/FDR/Chapter%201%20-%20Executive%20Summary%20and%20Project%20Overview.pdf
    (Table 1.1)
  reference2: ''
  reference3: ''
  comment: APS-U Brightness mode (324-bunch), rms values. Energy spread not given
    in this source and is assumed from similar sources. Compiled by Claude Sonnet
    5.0 (medium), verify before use for important calculations.
  emittance_hor: 41.16
  emittance_ver: 4.16
  phase_space_density: 1.1680496374373925
- name: Sirius High β
  energy: 3.0
  energy_spread: 0.085
  current: 350
  beamsize_hor: 64.9
  beamsize_ver: 3.4
  divergence_hor: 3.8
  divergence_ver: 0.7
  date: '2026-07-29'
  reference1: https://lnls.cnpem.br/accelerators/storage-ring-parameters/
  reference2: ''
  reference3: ''
  comment: Beam size/divergence at center of the long (7.5 m) straight section SS-A,
    a high-beta ID source point. Compiled by Claude Sonnet 5.0 (medium), verify before
    use for important calculations.
  emittance_hor: 246.62
  emittance_ver: 2.38
  phase_space_density: 0.5962972327038024
- name: PETRA IV TM 5m
  energy: 6.0
  energy_spread: 0.1
  current: 80
  beamsize_hor: 5.1
  beamsize_ver: 5.1
  divergence_hor: 2.3
  divergence_ver: 2.3
  date: 2026-10-09
  reference1: PETRA IV EDR, P. 46 and P. 68, draft version Nov 17 2025
  reference2: ''
  reference3: ''
  comment: PETRA IV Timing Mode, fully-coupled, in 5m straight sections (4.3m usable
    ID length)
  emittance_hor: 11.729999999999999
  emittance_ver: 11.729999999999999
  phase_space_density: 0.5814253497091785
- name: Sirius Low β
  energy: 3.0
  energy_spread: 0.085
  current: 350
  beamsize_hor: 19.1
  beamsize_ver: 2.0
  divergence_hor: 13.0
  divergence_ver: 1.3
  date: '2026-07-29'
  reference1: https://lnls.cnpem.br/accelerators/storage-ring-parameters/
  reference2: ''
  reference3: ''
  comment: Beam size/divergence at center of the short (6.5 m) straight section SS-B,
    a low-beta ID source point. Compiled by Claude Sonnet 5.0 (medium), verify before
    use for important calculations.
  emittance_hor: 248.3
  emittance_ver: 2.6
  phase_space_density: 0.5421481458533411
- name: ESRF-EBS
  energy: 6.0
  energy_spread: 0.093
  current: 200
  beamsize_hor: 30.18
  beamsize_ver: 4.37
  divergence_hor: 3.64
  divergence_ver: 1.37
  date: '2026-07-29'
  reference1: https://arxiv.org/pdf/1906.07100 (Table 4)
  reference2: https://link.aps.org/doi/10.1103/PhysRevAccelBeams.27.051601
  reference3: ''
  comment: Electron beam parameters at the center of the ID straight section (EBS
    lattice S28D); energy spread from ESRF-EBS Technical Report (9.3e-4). Compiled
    by Claude Sonnet 5.0 (medium), verify before use for important calculations.
  emittance_hor: 109.8552
  emittance_ver: 5.9869
  phase_space_density: 0.304093664723618
- name: APS-U TM
  energy: 6.0
  energy_spread: 0.1
  current: 200
  beamsize_hor: 12.9
  beamsize_ver: 8.8
  divergence_hor: 2.5
  divergence_ver: 3.7
  date: '2026-07-29'
  reference1: https://www.aps.anl.gov/sites/www.aps.anl.gov/files/APS-Uploads/Aps-Upgrade/FDR/Chapter%201%20-%20Executive%20Summary%20and%20Project%20Overview.pdf
    (Table 1.1)
  reference2: ''
  reference3: ''
  comment: APS-U Timing mode (48-bunch), rms values, optimized for single-bunch brightness/time-resolved
    experiments. and is assumed from similar sources. Compiled by Claude Sonnet 5.0
    (medium), verify before use for important calculations.
  emittance_hor: 32.25
  emittance_ver: 32.56
  phase_space_density: 0.19046530674437648
- name: MAX IV
  energy: 3.0
  energy_spread: 0.077
  current: 300
  beamsize_hor: 54
  beamsize_ver: 4
  divergence_hor: 6
  divergence_ver: 2
  date: '2026-08-14'
  reference1: https://journals.iucr.org/s/issues/2021/06/00/ye5008/ye5008.pdf (Johansson
    et al., J. Synchrotron Rad. 28, 1935-1947 (2021), Table 1)
  reference2: https://www.esrf.fr/files/live/sites/www/files/events/conferences/2022/ESLS%202022/MOLLOY_MAX%20IV_Operation%20%26%20upgrade%20status_economy%20plan.pdf
  reference3: ''
  comment: The numbers for the current are all over the place, 500mA is the design
    value, the second reference says 300mA is used for regular operation, but at the
    time of writing the machine status page says 200mA. I use 300mA as this is the
    value provided by the head of accelerator operation.
  emittance_hor: 324
  emittance_ver: 8
  phase_space_density: 0.11574074074074074
- name: PETRA III 10m
  energy: 6.0
  energy_spread: 0.1
  current: 100
  beamsize_hor: 141.6
  beamsize_ver: 6.6
  divergence_hor: 7.1
  divergence_ver: 1.5
  date: 2025-07-29
  reference1: https://photon-science.desy.de/facilities/petra_iii/machine/parameters/index_eng.html
  reference2: ''
  reference3: ''
  comment: ''
  emittance_hor: 1005.3599999999999
  emittance_ver: 9.899999999999999
  phase_space_density: 0.010047157337680137
- name: PETRA III 5m
  energy: 6.0
  energy_spread: 0.1
  current: 100
  beamsize_hor: 34.6
  beamsize_ver: 6.3
  divergence_hor: 28.9
  divergence_ver: 1.6
  date: 2025-07-29
  reference1: https://photon-science.desy.de/facilities/petra_iii/machine/parameters/index_eng.html
  reference2: ''
  reference3: ''
  comment: These are the low beta values
  emittance_hor: 999.9399999999999
  emittance_ver: 10.08
  phase_space_density: 0.009921230194446589
- name: Diamond
  energy: 3.0
  energy_spread: 0.1
  current: 300
  beamsize_hor: 123
  beamsize_ver: 6
  divergence_hor: 24
  divergence_ver: 4
  date: '2026-07-29'
  reference1: https://cas.web.cern.ch/sites/default/files/lectures/daresbury-2007/r-walker-diamond.pdf
  reference2: ''
  reference3: ''
  comment: Original Diamond design values at centre of a 5 m ID straight section (7
    mm ID gap), from R. Walker (Diamond Technical Director), CAS 2007. Diamond has
    since been operating with various lattice/current updates and is planned to be
    replaced by Diamond-II; these values are historical design figures, not necessarily
    current operational values. Energy spread was not provided and is assumed from
    similar sources.
  emittance_hor: 2952
  emittance_ver: 24
  phase_space_density: 0.004234417344173441
- name: PETRA II
  energy: 12.0
  energy_spread: 0.1
  current: 60
  beamsize_hor: 600
  beamsize_ver: 100
  divergence_hor: 24
  divergence_ver: 4.2
  date: '2026-08-06'
  reference1: https://proceedings.jacow.org/p95/ARTICLES/FAR/FAR07.PDF (Balewski et
    al., PAC 1995, Table 1)
  reference2: ''
  reference3: ''
  comment: 'DESY PETRA storage ring operated parasitically (during HERA-injector idle
    time) as a synchrotron radiation source from 1995-2007, using a single hard X-ray
    undulator (33 mm period) in straight section North East; this is the ring later
    rebuilt into PETRA III. Horizontal emittance 18 nm rad at 12 GeV with the low-emittance
    optic, 3% emittance coupling. Current: up to 55-60 mA design; energy spread not
    given in this source (assumed value is used here). Values are for the low-emittance
    undulator optic (as opposed to the standard 45-degree-phase-advance injection
    optic used for HERA injection, which had 18 nm rad emittance at 7 GeV). Compiled
    by Claude Sonnet 5.0 (medium), verify before use for important calculations.'
  emittance_hor: 14400
  emittance_ver: 420.0
  phase_space_density: 9.92063492063492e-06
- name: DORIS III
  energy: 4.5
  energy_spread: 0.11
  current: 140
  beamsize_hor: 3046.0
  beamsize_ver: 350.9
  divergence_hor: 134.6
  divergence_ver: 34.2
  date: '2026-08-06'
  reference1: https://cerncourier.com/a/the-three-lives-of-doris-from-charm-quarks-to-cell-biology/
  reference2: https://accelconf.web.cern.ch/p95/ARTICLES/FAA/FAA02.PDF (Nesemann et
    al., EPAC 1996)
  reference3: ''
  comment: The beta_x = 22.63 m and beta_y = 10.26 m values at an undulator-favored
    straight section with closed Wigglers were obtained E. Weckert with a custom RAG
    of internal documents. The remaining entries were retrieved by Claude Sonnet 5.0
    (medium). These values require verification before being used for any serious
    calculation.
  emittance_hor: 409991.6
  emittance_ver: 12000.78
  phase_space_density: 2.8454018039934957e-08
