#! /usr/bin/env python3

import os
from subprocess import check_output

def predicted_energy( dir_name ):
    return check_output( [ "corrdump", "-c", "-s={}/str.out".format( dir_name ), "-eci=eci.out" ] )

for directory in os.walk( '.' ):
    dir_name = directory[0]
    if dir_name is not '.':
        dir_name = dir_name.split( '/' )[-1]
        energy = predicted_energy( dir_name ).decode( 'utf-8' ).strip()
        print( "{} {}".format( dir_name, energy ) )

