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

You will need to obtain a small topography DEM needed for this example:

    make topo
    
(or equivalently, `python fetch_topo.py`, which fetches the topo file from
a GeoClaw archive).

Execute these commands:

    make new   # compile Geoclaw code starting from scratch
    make data  # converts information in setrun.py into various *.data files
    make output  # runs the Fortran code using data in *.data files
    make plots  # creates _plots with plots specified by setplot.py
    
If running on your own laptop, you can then open _plots/_PlotIndex.html
in a web browser to view the plots.

On the JupyterHub, you can view selected plots by opening the notebook
ViewPlotsQuillayute.ipynb.  A rendered version of what that should look
like can be viewed in the archived version [ViewPlotsQuillayute.html](https://faculty.washington.edu/rjl/misc/quillayute/ViewPlotsQuillayute_2024-05-09.html).

## Notes on the setup:

The topography DEM Quillayute_13s.asc comes from a previous tsunami study
and is referenced to MHW (mean high water), and so setting sea_level = 0
in setrun.py corresponds to the initial water level at MHW.
To investigate different tide stages, see the
[Datums for the NOAA Tide Gauge at La Push](https://tidesandcurrents.noaa.gov/datums.html?datum=MLLW&units=1&epoch=0&id=9442396&name=La+Push%2C+Quillayute+River&state=WA) for differences in elevation between tide stages.

This DEM has 1/3 arc-second horizontal resolution (roughly 10 m in longitude
and 7 m in latitude). In principle,
the [NCEI Continuously Updated Digital Elevation Model (CUDEM) - 1/9 Arc-Second Resolution Bathymetric-Topographic Tiles](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ngdc.mgg.dem:999919)
should provide more recent data (referenced to NAVD88), but it seems to have
questionable data near the Quillayute River, which needs more investigation.
Obtaining accurate DEMs is often the hardest part of setting up a GeoClaw run.
This is particularly true in river valleys where the topography frequently
changes.

The river flow is set up by specifying a source of water over some small
rectangle chosen to be in the river, and then running the code until
the river reaches a steady state.  This is accomplished by providing
the subroutine src2.f90 that includes this source term.  The discharge of
the river is specified in this routine. Varying this value would change the
resulting steady state flow.

## Add a flooding event

The initial run specified in setrun.py if for only 1 hour and sets up an
approximate steady state flow in the river (2 or 3 hours would be better, 
but here we want it to run quickly).

Another set of files allows doing a longer run that not only includes the
for the river but also a source term over the entire eastern portion
of the domain that can be viewed as a major precipitation event.

Water is added at the rate of 2 m per hour for 15 minutes, so total
rainfall of 0.5 meters, which then flows into the river and through other
stream channels.  (**NOTE:** It is not clear that the shallow water equations
with the bottom friction term used in GeoClaw is suitable for modeling rain
runoff and we are ignoring infiltration, subsurface flow, etc.  This is simply
done here as an easy way to generate a flood in the river!)

This modified source term is in the Fortran code `src2_flood.f90`, and the
setrun_flood.py specifies the running conditions.

To run the modified code:

    make data  -f Makefile_flood  # to update the *.data files
    make .plots -f Makefile_flood
    
The latter command should compile a new version of the code
using src2_flood.f90 (producing a new executable xgeoclaw_flood),
and do a new run using the data in setrun_flood.py.

The output will go into _output_flood and the new plots will go in _plots_flood.
All of this is specified in Makefile_flood.

Besides the additional source term, the following things changed in setrun:

 - The output times are now specified using output_style 2 as every 15 minutes
   for the first hour and then every 5 minutes up to 1.5 hours.
    
 - Refinement regions are adjusted so that only two levels of refinement
   are allowed in the rainfall region (except around the river source).
   This is simply to make the code run more quickly since we just want to see
   the effect downstream.
   
Note that in practice one might do a longer run to set up the steady state
river conditions and then use the checkpoint file generated at the end of that
run as the starting point for several different tests with rainfall, a tsunami,
storm surge, or upstream dam break added at later times.
