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
import time
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

def WeightedOverlay(bohLayer,bohLayer1):
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\OUTPUT.tif"

    entries = []
    #define band 1
    boh1=QgsRasterCalculatorEntry()
    boh1.ref='boh@1'
    boh1.raster=bohLayer
    boh1.bandNumber=1
    entries.append(boh1)

    #define band 2
    boh2=QgsRasterCalculatorEntry()
    boh2.ref='boh1@1'
    boh2.raster=bohLayer1
    boh2.bandNumber=1
    entries.append(boh2)

# Process calculation with input extent and resolution
    calc =QgsRasterCalculator('Float(boh1@1 - boh@1)/Float(boh1@1 + boh@1)','outputfile','GTiff', bohLayer.extent(), bohLayer.width(), bohLayer.height(), entries )
    calc.processCalculation()










    
    
    
    '''
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\OUTPUT.tif"
    parameters = {'INPUT_A' :A,B\
    'FORMULA': A*20+B*80\
    'OUTPUT': tfile}
    processing.run('gdal:rastercalculator', parameters)   
    rlayer = QgsRasterLayer(tfile,"OUTPUT")
    return rlayer,tfile


    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\OUTPUT.tif"
    Map=processing.run("saga:orderedweightedaveraging", 
        {'GRIDS':[A,B],\
        'WEIGHTS':[50,50],\
        'OUTPUT':tfile})
    rlayer = QgsRasterLayer(tfile,"OUTPUT")
    return rlayer,tfile

    '''
'''
def WeightedOverlay(RRoadDC_Reclass,RTrans_DC_Reclass,R_LandCo_reclass,R_PopDe_Reclass,R_Solar_Reclass,RCDC_reclassify,Road_W,Transmis_W,LandC_W,PopDe_W,Solar_W,City_W):
    tf = tempfile.TemporaryDirectory()
    tfile = tf.name + "\\OUTPUT.sdat"
    Map=processing.run("saga:orderedweightedaveraging", 
        {'GRIDS':[RRoadDC_Reclass,RTrans_DC_Reclass,R_LandCo_reclass,R_PopDe_Reclass,R_Solar_Reclass,RCDC_reclassify],\
        'WEIGHTS':[Road_W,Transmis_W,LandC_W,PopDe_W,Solar_W,City_W],\
        'OUTPUT':tfile})
    rlayer = QgsRasterLayer(tfile,"OUTPUT")
    return rlayer,tfile
    
    processing.run("saga:orderedweightedaveraging", {'GRIDS':['G:/GISA-Project/New/Classify/BuildingC.tif','G:/GISA-Project/New/Classify/EnvironmentSeC.tif','G:/GISA-Project/New/Classify/HydrologyC.tif'],
    'WEIGHTS':[10,20,70],
    'OUTPUT':'C:/Users/Prasadi/AppData/Local/Temp/processing_e658f7422b3540ebb41e2d5734445fdc/aff7c63b9aa2465fb8b1b6cbd8650da7/OUTPUT.sdat'})
    


    TotWeight=0
    for i in range(0, len(a)):
        sum[i]=a[i]*b[i]
        TotWeight=TotWeight+b[i]
    for i in range (0,len(sum)):
        sum
    '''