
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

import numpy as np
import matplotlib.pyplot as plt

from clawpack.geoclaw import topotools

# River source region:
x1rs = -124.577
x2rs = -124.5750
y1rs = 47.9097
y2rs = 47.9106

def add_rs_box(current_data):
    from clawpack.visclaw.plottools import plotbox
    plotbox([x1rs,x2rs,y1rs,y2rs],
            kwargs={'color':'yellow', 'linewidth':1})


#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from clawpack.visclaw import colormaps, geoplot
    from numpy import linspace

    plotdata.clearfigures()  # clear any old figures,axes,items data


    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    def addgauges(current_data):
        from clawpack.visclaw import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=True)
             
    dark_blue = [0.2,0.2,0.7];
    light_blue = [0.5,0.5,1.0];
    blue = [0.0,0.0,1.0];
    blue_green = [0.0,1.0,1.0]

    cmap_flooding = colormaps.make_colormap({0: blue_green,
                                             0.5: light_blue,
                                             1: blue})

    yellow = [1.0,0.8,0.2]
    red = [1.0,0.0,0.0]
    cmap_speed = colormaps.make_colormap({0: blue_green,
                                          0.5: yellow,
                                          1: red})
                                          
    #-----------------------------------------
    # Figure for depth
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Domain depth', figno=0)
    plotfigure.figsize=(12,4)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Depth at time h:m:s'
    plotaxes.scaled = True
    plotaxes.xlimits = [-124.66, -124.57]
    plotaxes.ylimits = [47.90, 47.93]
    plotaxes.useOffset = False
    plotaxes.xticks_kwargs = {'rotation':20}
    plotaxes.afteraxes = add_rs_box


    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.depth
    #plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmap = cmap_flooding
    plotitem.pcolor_cmin = 0.
    plotitem.pcolor_cmax = 3.
    plotitem.add_colorbar = True
    plotitem.colorbar_shrink = 0.5
    plotitem.colorbar_extend = 'max'
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 1


    #-----------------------------------------
    # Figure for depth - zoom view
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='La Push depth', figno=1)
    plotfigure.figsize=(10,5)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Depth at time h:m:s'
    plotaxes.scaled = True
    plotaxes.xlimits = [-124.645, -124.6]
    plotaxes.ylimits = [47.905, 47.925]
    plotaxes.useOffset = False
    plotaxes.xticks_kwargs = {'rotation':20}
    plotaxes.afteraxes = addgauges


    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.depth
    plotitem.pcolor_cmap = cmap_flooding
    plotitem.pcolor_cmin = 0.
    plotitem.pcolor_cmax = 3.
    plotitem.add_colorbar = True
    plotitem.colorbar_shrink = 0.5
    plotitem.colorbar_extend = 'max'
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    #-----------------------------------------
    # Figure for speed
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Domain speed', figno=10)
    plotfigure.figsize=(12,4)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Speed at time h:m:s'
    plotaxes.scaled = True
    plotaxes.xlimits = [-124.66, -124.57]
    plotaxes.ylimits = [47.90, 47.93]
    plotaxes.xticks_kwargs = {'rotation':20}
    plotaxes.useOffset = False
    plotaxes.afteraxes = add_rs_box


    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.speed
    plotitem.pcolor_cmap = cmap_speed
    plotitem.pcolor_cmin = 0.
    plotitem.pcolor_cmax = 2.
    plotitem.add_colorbar = True
    plotitem.colorbar_shrink = 0.5
    plotitem.colorbar_label = 'm/s'
    plotitem.colorbar_extend = 'max'
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 1


    #-----------------------------------------
    # Figure for speed - zoom
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='La Push speed', figno=11)
    plotfigure.figsize=(10,5)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Speed at time h:m:s'
    plotaxes.scaled = True
    plotaxes.xlimits = [-124.645, -124.6]
    plotaxes.ylimits = [47.905, 47.925]
    plotaxes.useOffset = False
    plotaxes.xticks_kwargs = {'rotation':20}
    plotaxes.afteraxes = addgauges


    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.speed
    plotitem.pcolor_cmap = cmap_speed
    plotitem.pcolor_cmin = 0.
    plotitem.pcolor_cmax = 2.
    plotitem.add_colorbar = True
    plotitem.colorbar_shrink = 0.5
    plotitem.colorbar_label = 'm/s'
    plotitem.colorbar_extend = 'max'
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface at gauges', figno=300, \
                    type='each_gauge')
    plotfigure.figsize = (10,4)
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'Surface'
    plotaxes.grid = True
    plotaxes.time_scale = 1/60.  # plot in minutes
    plotaxes.time_label = 'minutes'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.show = False

    def gaugetopo(current_data):
        q = current_data.q
        h = q[0,:]
        eta = q[3,:]
        topo = eta - h
        return topo

    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'

    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata
