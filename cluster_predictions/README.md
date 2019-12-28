This directory contains predictive calculations of the energies of all symmetry inequivalent 2x2x2 supercells of TiOF2. The energies are estimated using the cluster expansion fitted in `../cluster_expansion/`, with the files `lat.in`, `clusters.out`, `eci.out`, and `ref_energy.out` symbolically linked from that directory.

The script `get_structures.py` is used to read generated POSCAR files from `../configurations/poscars` and create corresponding numbered directories containing `maps` `str.out` files, e.g. 

```
./get_structures.py 1360 --configdir ../configurations/poscars --supercell 2 2 2
```
, TODO: What is happening in this directory? Are the maps directories set up automatically?

`get_structures.py` previously set up all directories:

```
config_dir = '../configurations'
coordinate_type = 'Direct'
output_opts = { 'label'    : 4,
                'numbered' : False,
                'coordinates_only' : True }
 
poscars = glob.glob( config_dir + '/*.poscar' )
for poscar in poscars:
    search = re.search("\\d+", poscar , re.S)
    if search:
        nid = search.group()
        if not os.path.isdir( nid ):
            os.mkdir( nid )
        this_poscar = Poscar()
        this_poscar.read_from( poscar )
        this_poscar.coordinates *= np.array( [ 2.0, 2.0, 2.0 ] )
        filename = nid + '/str.out' 
        with open( filename, 'w' ) as f:
            f.write( "3.798000 0.000000 0.000000\n0.000000 3.798000 0.000000\n0.000000 0.000000 3.79
            sys.stdout = open( filename, 'a')
            this_poscar.output( coordinate_type = coordinate_type, opts = output_opts )
```
