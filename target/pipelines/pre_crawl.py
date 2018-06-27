import os
from os.path import dirname
import sys

current_folder = dirname(dirname(sys.argv[0]))
path = os.path.join(current_folder, "raw_data", "data.jl")
try:
    os.remove(path)
except Exception, ex:
    print "Cannot delete '%s' file" % path
