
from pylab import *
from clawpack.geoclaw import kmltools, topotools


name = 'Quillayute_13s'
topo = topotools.Topography('%s.asc' % name, topo_type=3)

kmltools.topo2kmz(topo, zlim=(-20,20), mask_outside_zlim=True, sea_level=0.,
             name=name, force_dry=None, close_figs=True)

