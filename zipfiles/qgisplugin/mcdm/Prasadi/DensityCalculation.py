from osgeo import gdal
from osgeo.gdalconst import *
from qgis.gui import *
from qgis.core import *

# Initialize Qt resources from file resources.py
from .resources import *
import os.path
import processing
import os
import tempfile

def DensityCal(infile):
    fields = infile.pendingFields()
    field_names = [field.name() for field in fields]
    if field in ['Population','POP','Pop']:
        