# Cluster expansion using MAPS

Two Python scripts to set up the input data for running calculating a cluster expansion using MAPS.

Running `setup_cluster_expansion.py` reads the `vasp_summary.yaml` dataset, and for each VASP calculation, extracts the configuration number and the energy. This script then calls the `copy_poscar_as_str_out()` function in `get_structure.py`, which creates a numbered subdirectory, reads the appropraite starting structure POSCAR from `../configurations/poscars` and saves this structure in the format MAPS expects as `<nid>/str.out`. The script then writes the energy for this configuration to `<nid>/energy`.

`maps` can then be run using e.g. `maps -d &` to calculate the cluster expansion. `maps` also needs a `lat.in` file which contains:
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
