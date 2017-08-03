#! /usr/bin/env python3

import glob
import re
import os
from vasppy.poscar import Poscar
import sys
import numpy as np

config_dir = '../configurations'
coordinate_type = 'Direct'
output_opts = { 'label'    : 4,
                'numbered' : False,
                'coordinates_only' : True }

if sys.argv[1]:
    nid = sys.argv[1]
else:
    raise

if not os.path.isdir( nid ):
    os.mkdir( nid )
this_poscar = Poscar()
this_poscar.read_from( "{}/config_{}.poscar".format( config_dir, nid ) )
this_poscar.coordinates *= np.array( [ 2.0, 2.0, 2.0 ] )
filename = nid + '/str.out' 
with open( filename, 'w' ) as f:
    f.write( "3.798000 0.000000 0.000000\n0.000000 3.798000 0.000000\n0.000000 0.000000 3.798000\n2.000000 0.000000 0.000000\n0.000000 2.000000 0.000000\n0.000000 0.000000 2.000000\n" )
    sys.stdout = open( filename, 'a')
    this_poscar.output( coordinate_type = coordinate_type, opts = output_opts )
