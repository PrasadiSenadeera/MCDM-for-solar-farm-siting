#Raster Clip tool

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

def RasterClip(infile,cliper):
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\Rasterclip.tif"
    area=cliper.extent()
    processing.run("gdal:cliprasterbyextent",\
    {'INPUT':infile,\
    'PROJWIN':area,\
    'NODATA':None,'OPTIONS':'',\
    'DATA_TYPE':0,\
    'OUTPUT':tfile})
    rlayer = QgsRasterLayer(tfile, "Rasterclip")
    return rlayer
