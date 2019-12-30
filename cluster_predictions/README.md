## TiOF<sub>2</sub> 2&times;2&times;2 supercell energies from the cluster expansion model

This directory contains predictive calculations of the energies of all symmetry inequivalent 2x2x2 supercells of TiOF2. The energies are estimated using the cluster expansion fitted in `../cluster_expansion/`, with the files `lat.in`, `clusters.out`, `eci.out`, and `ref_energy.out` symbolically linked from that directory.

The script `get_structures.py` is used to read generated POSCAR files from `../configurations/poscars` and create corresponding numbered directories containing `maps` `str.out` files, e.g. 

```
./get_structures.py 1360 --configdir ../configurations/poscars --supercell 2 2 2
```

To set up directories for all 2664 symmetry inequivalent 2&times;2&times;2 supercells:
```
for i in {0000..2663}; do ./get_structures.py $i --configdir ../2x2x2_configurations/poscars --supercell 2 2 2; done
```

The energies of these 2&times;2&times;2 supercells are evaluated using the `evaluate_energies.py` script. This script sequentially runs the MAPS [`corrdump`][corrdump] command on each of the supercell `str.out` files, using the effective cluster interactions generated in the [`../cluster_expansion`](../cluster_expansion) directory.

The `evaluate_energies.py` script requires the following files to be present:
- `lat.in`: ATAT lattice file.
- `clusters.out`: ATAT clusters file.
- `eci.out`: ATAT effective cluster interactions file.
- `ref_energy.out`: Reference energies to map the cluster-expansion energies to aligned DFT energies.
These files should be symlinked or copied from the [`../cluster_expansion`](../cluster_expansion) directory.

The `evaluate_energies.py` script can be run using:
```
./evaluate_energies.py > energies.out
```
This writes the output to `energies.out`. The output consists of three columns  
configuration ID // predicted energy // DFT energy (if this has been calculated)

Running the script also produces `corrdump.log`, `sym.out`, `maps.log`, and `strlist.out` files, which can be deleted.

[corrdump]: https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/manual/node35.html
