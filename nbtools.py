"""
Useful tools for running Clawpack from a Jupyter notebook.

This version also includes tools for viewing plots created via `make .plots`
if you are unable to open the html file `_plots/_PlotIndex.html`.
"""

import os
from IPython.core.display import display
from IPython.display import HTML

try:
    from IPython.display import FileLink
except:
    print("*** Ipython version does not support FileLink")


def make_driver(args, env, outfile, verbose):

    """
    Use subprocess to run a make command and capture the output.

    :Input:
    - *args*: arguments to the make command
    - *env*: environment to run in (if None, use *os.environ*)
      Useful if $CLAW must be set in notebook.
    - *outfile*: file name of file for capturing stdout and stderr
    - *vervose*: if True, print out command and display link to output file
    
    If the return code is non-zero, print a warning and link to output file
    regardless of value of *verbose*.

    """

    import subprocess
    import os, sys

    if env is None:
        env = os.environ

    if verbose:
        print("Executing shell command:   make %s" % args)
        sys.stdout.flush()

    ofile = open(outfile,'w')
    cmd_list = ['make'] + args.split()
    job = subprocess.Popen(cmd_list, stdout=ofile,stderr=ofile,env=env)
    return_code = job.wait()
    errors = (return_code != 0)
    if errors:
        print("*** Possible errors, return_code = %s" % return_code)
    
    if verbose or errors:
        local_file = FileLink(outfile)
        print("Done...  Check this file to see output:") 
        display(local_file)

def make_htmls(outfile=None, env=None, verbose=False, readme_link=True):
    """Perform 'make .htmls' and display link."""
    
    if outfile is None:
        outfile='htmls_output.txt'

    args = '.htmls'

    make_driver(args, env, outfile, verbose)

    if readme_link:
        print("See the README.html file for links to input files...")
        display(FileLink('README.html'))
    
def make_data(env=None, verbose=True):
    """Perform 'make data' and display link."""
    
    outfile='data_output.txt'
    args = 'data'
    make_driver(args, env, outfile, verbose)

def make_exe(new=False, env=None, verbose=True):
    """
    Perform 'make .exe' and display link.
    If *new = True*, do 'make new' instead to force recompilation of everything.
    """
    
    outfile='compile_output.txt'
    if new:
        args = 'new'
    else:
        args = '.exe'

    make_driver(args, env, outfile, verbose)

    
def make_output(label=None, env=None, verbose=True):
    """Perform 'make output' and display link."""
    
    if label is None: 
        label = ''
    else:
        if label[0] != '_':
            label = '_' + label
    outdir = '_output%s' % str(label)
    outfile = 'run_output%s.txt' % str(label)

    args = 'output OUTDIR=%s' % outdir
    make_driver(args, env, outfile, verbose)

    return outdir

    
def make_plots(label=None, env=None, verbose=True):
    """Perform 'make plots' and display links"""

    if label is None: 
        label = ''
    else:
        if label[0] != '_':
            label = '_' + label
    outdir = '_output%s' % str(label)
    plotdir = '_plots%s' % str(label)
    outfile = 'plot_output%s.txt' % str(label)

    args = 'plots OUTDIR=%s PLOTDIR=%s' % (outdir,plotdir)
    make_driver(args, env, outfile, verbose)

    if verbose:
        index_file = FileLink('%s/_PlotIndex.html' % plotdir)
        print("View plots created at this link:")
        display(index_file)

    return plotdir
    

def make_output_and_plots(label=None, env=None, verbose=True):

    outdir = make_output(label,env,verbose)
    plotdir = make_plots(label,env,verbose)
    return outdir,plotdir


def make_all(label=None, env=None, verbose=True):
    """Perform 'make all' and display links"""

    if label is None: 
        label = ''
    else:
        if label[0] != '_':
            label = '_' + label
    outdir = '_output%s' % str(label)
    plotdir = '_plots%s' % str(label)
    outfile = 'make_all_output%s.txt' % str(label)

    args = 'all OUTDIR=%s PLOTDIR=%s' % (outdir,plotdir)
    make_driver(args, env, outfile, verbose)

    if verbose:
        index_file = FileLink('%s/_PlotIndex.html' % plotdir)
        print("View plots created at this link:")
        display(index_file)

    return plotdir
    

# Tools to view plots from _plots if you cannot open _PlotIndex.html, e.g
# due to permission issues on a JupyterHub

def embed_html(elem, width_percent=50, height_pixels=None):
    """
    Create an html string to embed an element (png or html file) in notebook.
    The desired width is specified as width_percent of browser window.
    For large elements you might need to specify a height in pixels 
    for the scrolling window.
    
    Use HTML(embed_html(...)) to display in a notebook,
    or display(HTML(embed_html(...))) also works, and must be used
    if more than one thing is to displayed from the same cell.
    """
    if height_pixels is None:
        embed_html = f"<embed src='{elem}' width='{width_percent}%%'/>'"
    else:
        embed_html = f"<embed src='{elem}' width='{width_percent}%%'" \
                + f" height='{height_pixels}px' />"
    return embed_html

# Convenience functions to display frames, gauges, or animations that
# routinely appear in _plots:

def show_frame(frameno, figno=0, width_percent=50, height_pixels=None):
    elem = '_plots/frame%sfig%s.png' % (str(frameno).zfill(4), figno)
    if not os.path.isfile(elem):
        raise ValueError('%s not found' % elem)
    embed_frame  = embed_html(elem, width_percent, height_pixels)
    return display(HTML(embed_frame))

def show_gauge(gaugeno, figno=300, width_percent=50, height_pixels=None):
    elem = '_plots/gauge%sfig%s.png' % (str(gaugeno).zfill(4), figno)
    if not os.path.isfile(elem):
        raise ValueError('%s not found' % elem)
    embed_gauge  = embed_html(elem, width_percent, height_pixels)
    return display(HTML(embed_gauge))

def show_movie(figno=0, width_percent=70, height_pixels=800):
    elem = '_plots/movie_fig%s.html' % figno
    if not os.path.isfile(elem):
        raise ValueError('%s not found' % elem)
    embed_movie  = embed_html(elem, width_percent, height_pixels)
    return display(HTML(embed_movie))
