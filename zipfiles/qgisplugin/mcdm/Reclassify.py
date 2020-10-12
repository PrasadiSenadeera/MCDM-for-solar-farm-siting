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


def Reclassify(infile,order): 
    #driver = gdal.GetDriverByName('GTiff')
    provider = infile.dataProvider()
    extent = infile.extent()
    stats = provider.bandStatistics(1, QgsRasterBandStats.All) 
    k=stats.minimumValue
    b= stats.maximumValue-stats.minimumValue
    q=b/5
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\rules.txt"
    tfile2 = tf.name +"\\reclassify.tif"
    if order in ['From 1 to 5']:
        with open(tfile, 'w') as f:
            f.write('{0} thru {1} = 1\n'.format(  k,   k+q))
            f.write('{0} thru {1} = 2\n'.format(  k+q, k+2*q))
            f.write('{0} thru {1} = 3\n'.format(k+2*q, k+3*q))
            f.write('{0} thru {1} = 4\n'.format(k+3*q, k+4*q))
            f.write('{0} thru {1} = 5\n'.format(k+4*q, k+5*q))
    else:
        with open(tfile, 'w') as f:
            f.write('{0} thru {1} = 5\n'.format(  k,   k+q))
            f.write('{0} thru {1} = 4\n'.format(  k+q, k+2*q))
            f.write('{0} thru {1} = 3\n'.format(k+2*q, k+3*q))
            f.write('{0} thru {1} = 2\n'.format(k+3*q, k+4*q))
            f.write('{0} thru {1} = 1\n'.format(k+4*q, k+5*q))

    reclass=processing.run("grass7:r.reclass", {'input':infile,\
        'rules':tfile,\
        'txtrules':'',\
        'output':tfile2,\
        'GRASS_REGION_PARAMETER':infile.extent(),\
        'GRASS_REGION_CELLSIZE_PARAMETER':25,\
        'GRASS_RASTER_FORMAT_OPT':'','GRASS_RASTER_FORMAT_META':''})
    rlayer = QgsRasterLayer(tfile2, "reclassify")
    return rlayer,tfile2
     
   
   


