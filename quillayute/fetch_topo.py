
from clawpack.clawutil.data import get_remote_file

topo_fname = 'Quillayute_13s.asc'
url = 'http://depts.washington.edu/clawpack/geoclaw/topo/WA/' + topo_fname

get_remote_file(url, output_dir='.', file_name=topo_fname, verbose=True)
