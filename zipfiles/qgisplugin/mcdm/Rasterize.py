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
def Rasterize(infile,boundary,name):
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\Rasterisation.tif"
    area=boundary.extent()
    if name in ['PopDe']:
        raster=processing.run("gdal:rasterize",        
            {'INPUT':infile,\
            'FIELD':'POP_DE','BURN':1,'UNITS':0,\
            'WIDTH':1500,'HEIGHT':1500,\
            'EXTENT':area,\
            'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
            'INVERT':False,\
            'OUTPUT': tfile})
    elif name in ['LandCover']:
        raster=processing.run("gdal:rasterize",        
            {'INPUT':infile,\
            'FIELD':'Veg_Height','BURN':0,'UNITS':0,\
            'WIDTH':1500,'HEIGHT':1500,\
            'EXTENT':area,\
            'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
            'INVERT':False,\
            'OUTPUT':tfile})
    elif name in ['Solar']:
        raster=processing.run("gdal:rasterize",        
            {'INPUT':infile,\
            'FIELD':'VALUE','BURN':0,'UNITS':0,\
            'WIDTH':1500,'HEIGHT':1500,\
            'EXTENT':area,\
            'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
            'INVERT':False,\
            'OUTPUT':tfile})
    else:
        raster=processing.run("gdal:rasterize",        
            {'INPUT':infile,\
            'FIELD':None,'BURN':1,'UNITS':0,\
            'WIDTH':1500,'HEIGHT':1500,\
            'EXTENT':area,\
            'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
            'INVERT':False,\
            'OUTPUT': tfile})
    rlayer = QgsRasterLayer(tfile, "Rasterisation")
    return rlayer,tfile
        

    