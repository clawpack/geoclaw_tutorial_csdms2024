"""
Simple script to download topography/bathymetry data from thredds server

The CUDEM 1/9 arcsecond tiles are each 0.25 degree by 0.25 degree and the
name includes the lat-lon of the NW corner.

See:
https://www.ngdc.noaa.gov/thredds/dodsC/tiles/tiled_19as/ncei19_n48x00_w0124x75_2018v1.nc.html

"""

import os
from clawpack.geoclaw import topotools

plot_topo = True

server = 'https://www.ngdc.noaa.gov/thredds/dodsC/tiles/tiled_19as/'
tile = 'ncei19_n48x00_w0124x75_2018v1.nc'
url = server + tile

topo_dir = '.'

extent = [-124.661,-124.529,47.894,47.931]

if 0:
    # full 1/9" resolution
    coarsen = 1
    name = 'Quillayute_navd88_19s'
else:
    # subsample to 1/3" resolution
    coarsen = 3
    name = 'Quillayute_navd88_13s'

topo = topotools.read_netcdf(url, extent=extent,
                             coarsen=coarsen, verbose=True)

print('name = ',name)
fname = os.path.join(topo_dir, name + '.asc')
topo.write(fname, topo_type=3, header_style='asc',
                     grid_registration='llcenter', Z_format='%.2f')

print('Downloaded topo: %s' % fname)


if plot_topo:
    # plot the topo and save as a png file...
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots(figsize=(10,5))
    topo.plot(axes=ax,limits=[-20,20],
                cb_kwargs={'shrink':0.7, 'extend':'both'})
    plt.title('Topo file %s' % name)
    fname = name + '.png'
    fname = os.path.join(topo_dir, fname)
    plt.savefig(fname)
    print('Created %s' % fname)
