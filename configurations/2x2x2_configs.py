#! /usr/bin/env python3

import os
import numpy as np
from bsym.interface.pymatgen import unique_structure_substitutions
from pymatgen import Lattice, Structure
from pymatgen.io.vasp import Poscar

a = 3.798 # TODO: where does this latttice parameter come from?
poscar_dir = 'poscars'

coords = np.array( [ [ 0.0, 0.0, 0.0 ],
                     [ 0.5, 0.0, 0.0 ],
                     [ 0.0, 0.5, 0.0 ],
                     [ 0.0, 0.0, 0.5 ] ] )
atom_list = [ 'Ti', 'X', 'X', 'X' ]
lattice = Lattice.from_parameters( a=a, b=a, c=a, alpha=90, beta=90, gamma=90 )
unit_cell = Structure( lattice, atom_list, coords )

parent_structure = unit_cell * [ 2, 2, 2 ]
unique_structures = unique_structure_substitutions( parent_structure, 'X', { 'F':16, 'O':8 } )

print( "Found {} unique structures".format( len( unique_structures ) ) )

if not os.path.exists( poscar_dir ):
    os.makedirs( poscar_dir )

for i, s in enumerate( unique_structures ):
    poscar = Poscar( s.get_sorted_structure() )
    poscar.comment = "TiOF2 2x2x2 config {:04d}".format( i )
    poscar.write_file( "{}/config_{:04d}.poscar".format( poscar_dir, i ) )
