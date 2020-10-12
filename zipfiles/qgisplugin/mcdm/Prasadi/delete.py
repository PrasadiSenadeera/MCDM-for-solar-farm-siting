filename = self.dlg.lineEdit.text()
        with open(filename, 'w') as output_file:

        selectedLayerIndex = self.dlg.comboBox.currentIndex()
        selectedLayer = layers[selectedLayerIndex].layer()
        fieldnames = [field.name() for field in selectedLayer.fields()]
        # write header


        line = ','.join(name for name in fieldnames) + '\n'
        output_file.write(line)
        # wirte feature attributes
        for f in selectedLayer.getFeatures():
        line = ','.join(str(f[name]) for name in fieldnames) + '\n'
        output_file.write(line)

#raster layer extent calculate
        rlayer.extent().toString()
#vector layer extent calculate
        vlayer.extent().toString()


        joel
                road=self.dlg.comboBox.currentIndex()
        
        infile = ''
        outfile = ''

        ## Do the rasterization
        r.rasterize(infile, outfile)




        def create_layer(self):
                layers = list(QgsProject.instance().mapLayers().values())
                layers_name = [l.name() for l in layers]
                if not 'rev_lyr' in layers_name:
                # creates new 'rev_lyr' layer
                # note that this is memory layer and its not present
                # physically though it can be exported in desired format
                lyr = QgsRasterLayer("rev_lyr", "memory")
                # adds new 'rev_lyr' layer to the workspace
                QgsProject.instance().addMapLayer(lyr)



                
        #create new vector layer

            vl = QgsVectorLayer("Line", "Roads", "memory")
            pr = vl.dataProvider()


            processing.run("gdal:rasterize", {'INPUT':'E:\\NOVA\\Project\\Project_Seminar_Variables\\Prasadi\\TR_Transport_Li.shp','FIELD':None,'BURN':1,'UNITS':1,'WIDTH':25,'HEIGHT':25,'EXTENT':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]','NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,'INVERT':False,'OUTPUT':})
def prasadi(input,outfile):

     R_road = processing.run("qgis:rasterize",\
    {'INPUT':v1,\
    'FIELD':None,'BURN':1,'UNITS':1,\
    'WIDTH':10,'HEIGHT':10,\
    'EXTENT':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]',\
    'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
    'INVERT':False,\
    'OUTPUT':'C:/Users/Prasadi/AppData/Local/Temp/processing_e4879cf92f5242fabcd1862dad99fd85/1ae7c44fbb3d4092a729d2955ce70428/OUTPUT.tif'})
             
    processing.run("qgis:proximity",\
    {'INPUT':R_Road[OUTPUT],\
    'BAND':1,\
    'VALUES':'','UNITS':0,'MAX_DISTANCE':0,'REPLACE':0,\
    'NODATA':0,'OPTIONS':'',\
    'DATA_TYPE':5,\
    'OUTPUT':filename})

fill = processing.runalg("qgis:fillholes", input, 100000, None)



tf = tempfile.TemporaryDirectory()
tfolder = tf.name + "\\rasterisation.tif"
temp = processing.run("gdal:rasterize",
                       {'INPUT':v1,
                        'FIELD':None,'BURN':1,'UNITS':1,\
                        'WIDTH':10,'HEIGHT':10,\
                        'EXTENT':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]',\
                        'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
                        'INVERT':False,\
                        "OUTPUT": tfolder})
 rlayer = self.iface.addRasterLayer(tfolder, "Rasterisation")

         #call the rasterize 
            R_road = processing.run("gdal:rasterize",\
            {'INPUT':v1,\
            'FIELD':None,'BURN':1,'UNITS':1,\
            'WIDTH':10,'HEIGHT':10,\
            'EXTENT':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]',\
            'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
            'INVERT':False,\
            'OUTPUT':tfolder})
             


            tf = tempfile.TemporaryDirectory()
            tfolder = tf.name + "\\rasterisation.tif"
            R_Raster = processing.run("gdal:rasterize",
                {'INPUT':V_Road,\
                'FIELD':None,'BURN':1,'UNITS':1,\
                'WIDTH':10,'HEIGHT':10,\
                'EXTENT':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]',\
                'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
                'INVERT':False,\
                'OUTPUT': tfolder})
            
            tfolder = tf.name + "\\rasterdistance.tif"
            R_Raster_Distance = processing.run("gdal:proximity",\
                {'INPUT':R_Raster['OUTPUT'],\
                'BAND':1,\
                'VALUES':'','UNITS':0,'MAX_DISTANCE':0,'REPLACE':0,\
                'NODATA':0,'OPTIONS':'',\
                'DATA_TYPE':5,\
                'OUTPUT':tfolder})


from PyQt5.QtCore import QFileInfo
import processing
from osgeo import gdal
import nunpy as np

def reclassify(infile):
    
    infile = gdal.Open('E:\NOVA\Project\test\Raster_Distance.tif')
    band=infile.GetRasterBand(1)
    lista = band.ReadAsArray()

    max_value = np.amax(lista)
    min_value = np.amin(lista)

    a=(max_value-min_value)/5

    # reclassification    
    lista[np.where( lista < a )] = 1
    lista[np.where((a < lista) & (lista < (2*a))) ] = 2
    lista[np.where(((2*a) < lista) & (lista < (3*a))) ] = 3
    lista[np.where(((3*a) < lista) & (lista < (4*a))) ] = 4
    lista[np.where( lista > (4*a) )] = 5
    
    # create new file
    file2 = driver.Create( 'raster.tif', file.RasterXSize , file.RasterYSize , 1)
    file2.GetRasterBand(1).WriteArray(lista)

    # spatial ref system
    proj = infile.GetProjection()
    georef = infile.GetGeoTransform()
    file2.SetProjection(proj)
    file2.SetGeoTransform(georef)
    file2.FlushCache()

    return file2

    #https://gis.stackexchange.com/questions/163007/raster-reclassify-using-python-gdal-and-numpy



import numpy, sys
from osgeo import gdal
from osgeo.gdalconst import *


# register all of the GDAL drivers
gdal.AllRegister()

# open the image
inDs = gdal.Open("c:/workshop/examples/raster_reclass/data/cropland_40.tif")
if inDs is None:
  print 'Could not open image file'
  sys.exit(1)

# read in the crop data and get info about it
band1 = inDs.GetRasterBand(1)
rows = inDs.RasterYSize
cols = inDs.RasterXSize

cropData = band1.ReadAsArray(0,0,cols,rows)

listAg = [1,5,6,22,23,24,41,42,28,37]
listNotAg = [111,195,141,181,121,122,190,62]

# create the output image
driver = inDs.GetDriver()
#print driver
outDs = driver.Create("c:/workshop/examples/raster_reclass/output/reclass_40.tif", cols, rows, 1, GDT_Int32)
if outDs is None:
    print 'Could not create reclass_40.tif'
    sys.exit(1)

outBand = outDs.GetRasterBand(1)
outData = numpy.zeros((rows,cols), numpy.int16)


for i in range(0, rows):
    for j in range(0, cols):

    if cropData[i,j] in listAg:
        outData[i,j] = 100
    elif cropData[i,j] in listNotAg:
        outData[i,j] = -100
    else:
        outData[i,j] = 0


# write the data
outBand.WriteArray(outData, 0, 0)

# flush data to disk, set the NoData value and calculate stats
outBand.FlushCache()
outBand.SetNoDataValue(-99)

# georeference the image and set the projection
outDs.SetGeoTransform(inDs.GetGeoTransform())
outDs.SetProjection(inDs.GetProjection())

del outData


