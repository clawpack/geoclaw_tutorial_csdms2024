# geoclaw_tutorial_csdms2024

### Materials for the GeoClaw Clinic, CSDMS 2024 Annual Meeting

https://github.com/clawpack/geoclaw_tutorial_csdms2024

#### Instructions for running examples on the JupyterHub:

To use the [CSDMS JupyterHub](https://csdms.colorado.edu/wiki/JupyterHub),
open this link:
    https://lab.openearthscape.org/
    
If you are registered for the Annual Meeting, login using the email address
you used to register and pick a password the first time you login.

This should get you into a JupyterLab (see https://jupyter.org/ for general
documentation).

Click the blue + tab in the upper left corner to get Launcher, from which
you can open a Terminal.

Whenever you open a terminal you should give these commands (or add them
to the end of the file `$HOME/.bashrc`):

    source activate clawpack
    export CLAW=$HOME/clawpack
    echo CLAW=$CLAW

Clawpack can be installed via these commands:

    cd $HOME
    git clone https://github.com/clawpack/clawpack.git
    cd clawpack
    git checkout v5.10.0  # most recent release
    git submodule init
    git submodule update
    pip install --no-build-isolation -e ./

These same commands should also work on a laptop.  There are other
installation options, but if you use pip make sure to use the
command above so that it does not discard the Fortran files after
installing.  See https://www.clawpack.org/installing_fortcodes.html.
    
You should now be ready to run Clawpack examples, e.g.

    cd $CLAW/geoclaw/examples/tsunami/chile2010
    make new  # should compile Fortran and create xgeoclaw
    make data  # should make *.data files
    make output # should run the code.
    
After running, you should also be able to make a bunch of plots via:

    make plots
    
but viewing the plots on the cluster is not see easy.
We will see how to use a Jupyter notebook for this purpose.
(Copy the file `csdms_clinic_2024/ViewPlots.ipynb` to the example
directory and modify it to view specific plots).

The plots for the chile2010 example can be viewed in the Clawpack gallery at
[this link](https://www.clawpack.org/gallery/_static/geoclaw/examples/tsunami/chile2010/_plots/_PlotIndex.html)

#### Instructions for obtaining the tutorial example:

In a JupyterHub terminal (or on your laptop if you have Clawpack installed):

    cd $HOME
    git clone https://github.com/clawpack/geoclaw_tutorial_csdms2024.git
    
which will clone this repository.

Then see the README.md file in the `geoclaw_tutorial_csdms2024/quillayute` directory.

### Rendered versions of the Jupyter notebooks:

- [ViewPlotsQuillayute.html](https://depts.washington.edu/clawpack/geoclaw/geoclaw_tutorial_csdms2024/quillayute/ViewPlotsQuillayute.html).

- [plot_fgmax.html](https://depts.washington.edu/clawpack/geoclaw/geoclaw_tutorial_csdms2024/quillayute/plot_fgmax.html).


## Some other sources of information discussed in the clinic:

- Some GeoClaw references: http://www.geoclaw.org

- Clawpack documentation: http://www.clawpack.org

- Gallery: http://www.clawpack.org/gallery

- Poster on Visualizing Ship Motion in Tsunami Currents:
  https://depts.washington.edu/ptha/CSDMS2024/

- D-Claw examples: https://dlgeorge.github.io/projects/

- D-Claw on Github: https://github.com/geoflows/dclaw
