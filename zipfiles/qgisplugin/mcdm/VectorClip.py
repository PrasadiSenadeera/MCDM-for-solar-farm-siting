#Vector Clip 
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

def VectorClip(infile,clipfile):
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\Vectorclip.shp"
    area=clipfile.extent()
    processing.run("native:extractbyextent", 
        {'INPUT':infile,\
        'EXTENT':area,\
        'CLIP':True,\
        'OUTPUT':tfile})
    vlayer = QgsVectorLayer(tfile, "Vectorclip")
    return vlayer