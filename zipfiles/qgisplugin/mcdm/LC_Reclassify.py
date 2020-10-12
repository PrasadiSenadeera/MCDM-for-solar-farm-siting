    
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

def LC_Reclassify(infile,order): 
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\rules.txt"
    tfile2 = tf.name +"\\reclassify.tif"
    if order in ['From 1 to 5']:
        with open(tfile, 'w') as f:
            f.write('{0} thru {1} = 1\n'.format(  0, 200))
            f.write('{0} thru {1} = 2\n'.format(200, 300))
            f.write('{0} thru {1} = 3\n'.format(300, 600))
            f.write('{0} thru {1} = 4\n'.format(600, 1000))
            f.write('{0} thru {1} = 5\n'.format(1000,4000))
    else:
        with open(tfile, 'w') as f:
            f.write('{0} thru {1} = 5\n'.format(  0, 200))
            f.write('{0} thru {1} = 4\n'.format(200, 300))
            f.write('{0} thru {1} = 3\n'.format(300, 600))
            f.write('{0} thru {1} = 2\n'.format(600, 1000))
            f.write('{0} thru {1} = 1\n'.format(1000,4000))

    reclass=processing.run("grass7:r.reclass", {'input':infile,\
        'rules':tfile,\
        'txtrules':'',\
        'output':tfile2,\
        'GRASS_REGION_PARAMETER':infile.extent(),\
        'GRASS_REGION_CELLSIZE_PARAMETER':25,\
        'GRASS_RASTER_FORMAT_OPT':'','GRASS_RASTER_FORMAT_META':''})
    rlayer = QgsRasterLayer(tfile2, "reclassify")
    return rlayer,tfile2