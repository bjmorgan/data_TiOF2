#! /usr/bin/env python3

from vasppy.calculation import *
from get_structures import copy_poscar_as_str_out
import numpy as np
import re

calcs = import_calculations_from_file( '../2x2x2_vasp_calculations/TiOF2_2x2x2_sample_data.yaml' )
supercell = np.array( [ 2, 2, 2 ] )
config_dir = '../2x2x2_configurations/poscars/'

for c in calcs.values():
    nid = re.search( 'config (\d{4})', c.title )[1]
    copy_poscar_as_str_out( nid, config_dir, supercell )
    with open( '{}/energy'.format( nid ), 'w' ) as f:
        f.write( '{}\n'.format( c.energy ) )
