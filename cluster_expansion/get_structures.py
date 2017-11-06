#! /usr/bin/env python3

import glob
import re
import os
from pymatgen.io.vasp import Poscar
import sys
import numpy as np
import argparse

def np_string( v ):
    return ' '.join( [ str(f) for f in v ] )

# Note: pymatgen > 2017.10.16 can handle this using pymatgen.io.atat.Mcsqs.to_string()
def structure_to_str_out( structure, filename, supercell ):
    with open( filename, 'w' ) as f:
        for v in structure.lattice.matrix:
            f.write( "{}\n".format( np_string( v / supercell ) ) )
        f.write( "{:f} 0.0 0.0\n0.0 {:f} 0.0\n0.0 0.0 {:f}\n".format( *supercell ) )
        for site in structure:
            f.write( "{} {}\n".format( np_string( site.frac_coords * supercell ), site.species_string ) )

def copy_poscar_as_str_out( nid, config_dir, supercell ):
    if not os.path.isdir( nid ):
        os.mkdir( nid )
    poscar = Poscar.from_file( "{}/config_{}.poscar".format( config_dir, nid ) )
    structure_to_str_out( poscar.structure, '{}/str.out'.format( nid ), supercell )

def parse_arguments():
    parser = argparse.ArgumentParser( description="Reads a VASP POSCAR file named `config_<n>.poscar` and creates a corresponding numbered directory containing the same structure as a maps `str.out` file" )
    parser.add_argument( 'n', type=str, help='Configuration number to copy.' )
    parser.add_argument( '--configdir', help='Location of directory containing configuration POSCAR files.', required=True )
    parser.add_argument( '--supercell', nargs=3, type=int, help='Supercell expansion.', required=True )
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    copy_poscar_as_str_out( nid=args.n, 
                            config_dir=args.configdir, 
                            supercell=np.array( args.supercell ) )
