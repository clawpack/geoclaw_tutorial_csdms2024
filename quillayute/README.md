# Quillayute River Example

Test problem setting up a steady state flow in the
[Quillayute River](https://en.wikipedia.org/wiki/Quillayute_River)
that flows into the Pacific Ocean at La Push, WA
(in the [Quileute Tribal Nation](https://quileutenation.org/)).

This is a region in danger of flooding, where remediation efforts are underway.
See for example
[this story](https://wildsalmoncenter.org/2019/12/09/restoring-the-quillayute-before-it-floods-la-push/),
which includes a good Google Earth image of the flooding region.

## Instructions for running:

If running on the CSDMS JupyterHub, first see the instructions in ../README.md
to open a terminal window and make sure that Clawpack and other needed tools
are available.

[Download topography?]

Execute these commands:

    make new   # compile Geoclaw code starting from scratch
    make data  # converts information in setrun.py into various *.data files
    make output  # runs the Fortran code using data in *.data files
    make plots  # creates _plots with plots specified by setplot.py
    
If running on your own laptop, you can then open _plots/_PlotIndex.html
in a web browser to view the plots.

On the JupyterHub, you can view selected plots by opening the notebook
ViewPlotsQuillayute.ipynb.  A rendered version of what that should look
like can be viewed in the archived version [ViewPlotsQuillayute.html](add_URL).

## Notes on the setup:

The topography DEM comes from the [NCEI Continuously Updated Digital Elevation Model (CUDEM) - 1/9 Arc-Second Resolution Bathymetric-Topographic Tiles](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ngdc.mgg.dem:999919).  
For this simple test case, a very small subset of one tile has been extracted
and also subsampled to 1/3 arc-second resolution.  The script fetch_topo.py
could be modified to extract a different extent or resolution.

The DEM is referenced to NAVD88.  Suppose we want to run this model when
the tide stage is at Mean Higher High Water (MHHW).  Then we need to set
sea_level in setrun.py to be this elevation relative to NAVD88.  According to
the [Datums for the NOAA Tide Gauge at La Push](https://tidesandcurrents.noaa.gov/datums.html?datum=MLLW&units=1&epoch=0&id=9442396&name=La+Push%2C+Quillayute+River&state=WA), 
NAVD88 is 0.440 m above MLLW while MHHW is 2.597 m above MLLW, and hence is
2.157 m above NAVD88.  This is the value of sea_level used.
