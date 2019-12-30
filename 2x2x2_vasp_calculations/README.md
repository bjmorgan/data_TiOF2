# DFT Geometry optimisation of a sample of 2&times;2&times;2 TiOF<sub>2</sub> supercells.

This directory contains inputs and outputs for DFT geometry optimsations of 65 TiOF<sub>2</sub> 2&times;2&times;2 supercells. These supercells were generated using the script in the [../2x2x2_configurations](../2x2x2_configurations) directory.

Each subfolder is numbered according to the unique numerical ID of the supercell configuration. Each calculation folder includes the following files:
- inputs:
    - `INCAR`: VASP input.
    - `POSCAR`: VASP input. Optimised geometry.
    - `KPOINTS`: VASP input
    - `POTCAR.spec`: Specifies the VASP pseudopotentials used.
- outputs:
    - `OUTCAR`: VASP output.
    - `vasprun.xml.gz`: VASP output.
- metadata:
    - `vaspmeta.yaml`: Additional metadata for each calculation.

The directory contains a file `TiOF2_2x2x2_sample_data.yaml`, which provides a human readable summary of the key calculation parameters and outputs (e.g. final energies). This file has been produced using the `vasp_summary` script from the [`vasppy`](https://github.com/bjmorgan/vasppy) package.
```
vasp_summary -r > TiOF2_2x2x2_sample_data.yaml
```

The directory also contains a script `get_poscars.py`, which collates the optimised `POSCAR` files from the VASP calculation subdirectories, and collects these in the `dft_poscars` subdirectory.
```
get_poscars.py
```
