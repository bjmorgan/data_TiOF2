#! /usr/bin/env python3

from collections import Counter
from pymatgen.io.vasp import Poscar
from pymatgen.util.coord_utils import get_angle

class CoordinationEnvironment:

    def __init__( self, site, neighbours ):
        self.site = site
        self.neighbours = neighbours

    @property
    def coordination_number( self ):
        return len( self.neighbours )

    def coordination_species( self ):
        return set( ( site.species_string for site in self.neighbours ) )

    def coordination_species_numbers( self ):
        return Counter( ( site.species_string for site in self.neighbours ) )
       
    def coordinated_sites_by_string( self, string ):
        return [ site for site in self.neighbours if site.species_string is string ]
 
poscar = Poscar.from_file("POSCAR")
structure = poscar.structure
cutoff = 2.2
edge_cutoff = 3.0

coordination_environments = [ CoordinationEnvironment( i, [ n[0] for n in nn ] ) for i, nn in zip( structure, structure.get_all_neighbors( cutoff ) ) ]

cn_counter = Counter()
for ce in coordination_environments:
    if ce.site.species_string == 'Ti':
        cn_counter[ ce.coordination_species_numbers()[ 'O' ] ] += 1
        
for cn in cn_counter:
    print( cn, cn_counter[ cn ] / sum( cn_counter.values() ) )
print( 'dominated by TiO2F4 coordination environments' )

symmetry_counter = Counter()
for ce in coordination_environments:
    if ce.coordination_species_numbers()[ 'O' ] == 2:
        i, j = ce.coordinated_sites_by_string( 'O' )
        symmetry_counter[ i.distance( j ) < edge_cutoff ] += 1

print( symmetry_counter )
print( 'all of these have edge-sharing O sites' )

angle_counter = Counter()
for ce in coordination_environments:
    if ce.coordination_species_numbers()[ 'O' ] == 2:
        i, j = ce.coordinated_sites_by_string( 'O' )
        angle = get_angle( i.coords - ce.site.coords, j.coords - ce.site.coords, units='degrees' )
        angle_counter[ 75.0 < angle < 105.0 ] += 1

print( angle_counter )

# Probabilities of a given Ti having x coordinated oxygen ions are given by the corresponding binomial distribution.

from scipy.stats import binom   
print( [ binom.pmf(x,6,1/3) for x in range(7) ] ) 
