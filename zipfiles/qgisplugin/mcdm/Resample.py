#Resampling

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

def Resample (infile,PixelSize):
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\resample.txt"
    processing.run("grass7:r.resample", 
        {'input':infile,\
        'output':tfile,\
        'GRASS_REGION_CELLSIZE_PARAMETER':PixelSize,\
        'GRASS_RASTER_FORMAT_OPT':'',\
        'GRASS_RASTER_FORMAT_META':''})
    rlayer = QgsRasterLayer(tfile, "resample")
    return rlayer

    