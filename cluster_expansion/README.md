# TiOF<sub>2</sub> Cluster expansion using MAPS

This directory contains inputs and outputs for fitting a cluster expansion model for TiOF<sub>2</sub>, using [MAPS][maps].

## Contents
- Scripts:
    - `setup_cluster_expansion.py`: Copies initial structures and geometry-optimised VASP DFT energies into e.g. `0000` numeric subdirectories.
    - `get_structures.py`: Support functions for copying VASP POSCAR structures and converting into ATAT `str.out` structure format.
- Inputs (automatically copied and converted using the `setup_cluster_expansion.py` script):
    - `lat.in`: [ATAT lattice geometry input file](https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/manual/node21.html).
    - Numbered directories, e.g. `0000`, `0001`, `1618`. Each input directory contains:
        - `str.out`: ATAT structure / lattice file.
        - `energy`: Geometry optimised DFT energy, in eV.
- [Outputs](https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/manual/node46.html):
    - `clusters.out`
    - `eci.out`
    - `fit.out`
    - `gs.out`
    - `gs_str.out`
    - `maps.log`
    - `predstr.out`
    - `ref_energy.out`

## Workflow
1. Running `setup_cluster_expansion.py` reads the `TiOF2_2x2x2_sample_data.yaml` summary file from the [`2x2x2_vasp_calculations`](../2x2x2_vasp_calculations) directory. For each VASP calculation, the script extracts the configuration number and the DFT energy. The script then calls the `copy_poscar_as_str_out()` function in `get_structures.py`, which creates a numbered subdirectory, reads the appropraite starting structure POSCAR from [`../2x2x2_configurations/poscars`](../2x2x2_configurations/poscars)  and saves this structure in the format MAPS expects as `<nid>/str.out`. The script then writes the energy for this configuration to `<nid>/energy`.
2. Providing `maps` has been installed, `maps` can then be run using e.g. `maps -d &` to calculate the cluster expansion. Details about the `maps` inputs and outputs are available with `maps -h`.

## `lat.int`
In addition to the structures and energies for the fitting dataset, `maps` needs a `lat.in` file that defines the reference lattice:
```
3.798 3.798 3.798 90 90 90
1.0 0.0 0.0
0.0 1.0 0.0
0.0 0.0 1.0
0.0 0.0 0.0 Ti
0.5 0.0 0.0 O,F
0.0 0.5 0.0 O,F
0.0 0.0 0.5 O,F
```

## Subsequent analysis
The key outputs used for further calculations are:
- `eci.out`: The effective cluster interactions for each cluster.
- `clusters.out`: The corresponding clusters.
- `ref_energy.out`: Reference energies. These are not needed to get energy orderings, but are required to directly compare predicted energies to VASP energies.

[maps]: https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/manual/node20.html
