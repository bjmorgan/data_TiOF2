# TiOF<sub>2</sub> structure prediction dataset

Author: Benjamin J. Morgan
ORCID: 0000-0002-3056-8233
 
This dataset contains a series of calculations performed to study the F/O disorder in TiOF2, and the consequences for local structure.

The top-level directory contains the following sub-directories:

- 2x2x2_configurations
- 2x2x2_vasp_calculations
- cluster_predictions
- cluster_expansion
- cluster_predictions
- cluster_ga_4x4x4

## Overview

### Symmetry analysis of 2x2x2 disordered supercells

For the initial study of the F/O disorder in TiOF2, we began by generating all symmetry-inequivalent 2x2x2 supercells with TiOF2 stoichiometry. This symmetry analysis and structure generation is performed by the script `2x2x2_configs.py` in the `configurations` directory, and uses the `bsym` Python module. The output is a set of 2664 symmetry-inequivalent structures, outputted as `VASP` `POSCAR` files. These are generated in the `configurations/poscars` directory, and are named `config_<number>.poscar`, where `<number>` is the configuration number for that structure.

### Geometry optimisation using `VASP`.
 
A subset of the 2664 symmetry-inequivalent structures generated by `bsym` were selected for full geomtry optimisation using density functional theory with `VASP`. These calculations used the `Ti_pv`, `O`, and `F` PAW pseudopotentials, with a Dudarev $+U$ term applied to the Ti $d$ states. PBEsol functional. Full geometry optimisations were performed, allowing cell shape and volume to change freely. Energy cutoff of 700 eV, and k-point sampling using a 4x4x4 Monkhorst-Pack k-point mesh. Struture optimsation was deemed converged when forces on all ions were smaller than 0.01 eV per Angstrom. Energies of the optimised structures were collated using the `vasp_summary.py` script (which relies on the `vasppy` Python module), and are listed in the `TiOF2_2x2x2_sample_data.yaml` files.

### Cluster expansion interaction fitting
[README](cluster_expansion/README.md)

### Checking low energy structures
[README](cluster_predictions/README.md)

### Genetic algorithm structure prediction of 4x4x4 disordered supercells.

TODO

#### notes
- +U corrections are not necessary for these calculations, but has been used here for consistency with other work, and to allow future defect calculations to be performed with consistent parameters.
- The data set also contains an equivalent set of calculations performed using a 2x2x2 Monkhorst-Pack k-point mesh).

## Requirements

### Python Modules

- `bsym`: Symmetry analysis of the disordered TiOF2 2x2x2 supercell.
- `pymatgen`: Handling structures, and converting to/from `VASP` `POSCAR` format.
- `vasppy`: Collating `VASP` calculation data.
- `beagle`: Optimisation of TiOF2 4x4x4 supercells by a genetic algorithm, using the cluster expansion as a model Hamiltonian.

### Other Codes

- [`VASP`](http://vasp.at/): All DFT geometry optimisations.
- `MAPS`, available as part of the [ATAT](https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/) suite of codes: Fitting the cluster expansion.
 
