#! /usr/bin/env python3

from pymatgen.io.vasp import Poscar 
from beagle import Population, Individual
from beagle.individual import crossover, mutate, matches
from beagle.interface.maps import structure_to_str_out, ref_energy, predicted_energy
import numpy as np
import random 
from functools import partial

def np_string(v):
    return ' '.join([str(f) for f in v])

def mutator( x ):
    for i in range(random.randint( 1, 10 )):
        y = swap(x, a=1, b=0)
        x = y
    return x

def swap( vector, a, b ):
    i = random.choice( matches( vector, a ) )
    j = random.choice( matches( vector, b ) )
    return np_swap( vector, i, j )

def np_swap( a, i, j ):
    b = np.copy( a )
    b[i] = a[j]
    b[j] = a[i]
    return b

template_poscar = 'initial_structure.poscar' 
poscar = Poscar.from_file( template_poscar )
structure = poscar.structure
disordered_site_label = 'O'
elements = { 1: 'O', 0: 'F' }

def new_structure_from_vector( v ):
    new_structure = structure.copy()
    for site, sub in zip( structure.indices_from_symbol( disordered_site_label ), v ):
        new_structure[ site ] = elements[ sub ]
    new_structure.sort()
    return new_structure

def fitness_function( v, n_atoms, expansion, ref_eng ):
    new_structure = new_structure_from_vector( v )
    structure_to_str_out( new_structure, 'str.out', expansion )
    pe = predicted_energy( n_atoms, ref_eng, np.product( expansion ) )
    return( pe )

def next_generation( population, fitness_function ):
    population.sort()
    best = population[0]
    n_offspring = 120
    new_population = Population( [ best ] )
    while len( new_population ) < n_offspring:
        a, b = population.sample( 2 )
        c = crossover(a, b)
        c.constrain(target = {1:64, 0:128})
        if random.random() < 0.15:
            try:
                d = mutate( c, mutator )
            except:
                d = c
            c = d
        if c not in new_population:
            new_population += c
    selected = Population( new_population.boltzmann( fitness_function, temp=750.0, size=40 ) )
    return selected

def structure_to_str_out( structure, filename, supercell ):
    with open( filename, 'w' ) as f:
        for v in structure.lattice.matrix:
            f.write( "{}\n".format( np_string( v / supercell ) ) )
        f.write( "{:f} 0.0 0.0\n0.0 {:f} 0.0\n0.0 0.0 {:f}\n".format( *supercell ) )
        for site in structure:
            f.write( "{} {}\n".format( np_string( site.frac_coords * supercell ), site.species_string ) )

if __name__ == '__main__':
    niter = 500
    expansion = np.array( [ 4, 4, 4 ] )
    ref_eng = ref_energy()
    n_atoms = 3
    p1 = Population()
    args = ( n_atoms, expansion, ref_eng )
    a = np.array( [ 1 ] * 64 + [ 0 ] * 128 )
    f = partial( fitness_function, n_atoms=n_atoms, expansion=expansion, ref_eng=ref_eng )
    for i in range( 40 ):
        np.random.shuffle( a )
        p1 += Individual( a.copy() )
    p1.fitness_scores( f )
    print( "{} {:.4f} {}".format( 0, np.mean( p1.scores ),  np_string( np.sort( p1.scores ) ) ), flush=True )
    for i in range( niter ):
        p2 = next_generation( p1, f )
        p1 = p2
        print( "{} {:.4f} {}".format( i+1, np.mean( p1.scores ),  np_string( np.sort( p1.scores ) ) ), flush=True )
    opt_structure = new_structure_from_vector( sorted( p1.individuals, key=lambda i: i.fitness_score( f ) )[0].vector )
    Poscar( opt_structure ).write_file( "opt.poscar" )
    structure_to_str_out( opt_structure, 'opt_str.out', expansion ) 

