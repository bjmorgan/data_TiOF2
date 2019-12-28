#! /usr/bin/env python3

import glob
import re
from shutil import copyfile

contcar_paths = glob.glob('*/CONTCAR')
config_re = re.compile('config_(\d+)/CONTCAR')
for p in contcar_paths:
    config_id = config_re.findall( p )[0]
    copyfile( p, 'dft_poscars/config_{}.poscar'.format( config_id ) )

    


