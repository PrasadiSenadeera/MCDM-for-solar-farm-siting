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

def RasterDistance(infile):
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\Rasterdistance.tif"
    raster_distance=processing.run("gdal:proximity",\
        {'INPUT':infile,\
        'BAND':1,\
        'VALUES':'','UNITS':0,'MAX_DISTANCE':0,'REPLACE':0,\
        'NODATA':0,'OPTIONS':'',\
        'DATA_TYPE':5,\
        'OUTPUT':tfile})
    rlayer = QgsRasterLayer(tfile, "Rasterdistance")
    return rlayer
     