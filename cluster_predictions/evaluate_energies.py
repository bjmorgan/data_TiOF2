#! /usr/bin/env python3

import os
from subprocess import check_output

dft_energy_dir = '../cluster_expansion'

n_atoms = 3 # TODO this should be pulled from somewhere
expansion = 2*2*2

def ref_energy():
    with open( 'ref_energy.out' ) as f:
        return float( f.readlines()[0] )

def predicted_energy( dir_name ):
    output = check_output( [ "corrdump", "-c", "-s={}/str.out".format( dir_name ), "-eci=eci.out" ] )
    return float( output.decode( 'utf-8' ).strip() )

def dft_energy( dir_name ):
    try:
        with open( '{}/{}/energy'.format( dft_energy_dir, dir_name ) ) as f:
            return float( f.readlines()[0] )
    except:
        return None 

ref_eng = ref_energy()
for directory in os.walk( '.' ):
    dir_name = directory[0]
    if dir_name is not '.':
        dir_name = dir_name.split( '/' )[-1]
        energy = predicted_energy( dir_name )
        dft_e = dft_energy( dir_name )
        print( "{} {} {}".format( dir_name, ( energy + ref_eng * n_atoms ) * expansion, dft_e ) )

