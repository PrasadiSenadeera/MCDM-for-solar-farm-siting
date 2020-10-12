import processing

def euclidean (infile,outfile):

    tf = tempfile.TemporaryDirectory()
    tfolder = tf.name + "\\rasterisation.tif"
    R_Raster = processing.run("gdal:rasterize",
        {'INPUT':infile,
        'FIELD':None,'BURN':1,'UNITS':1,\
        'WIDTH':10,'HEIGHT':10,\
        'EXTENT':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]',\
        'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
        'INVERT':False,\
        "OUTPUT":tfolder})      
        #tfolder = tf.name + "\\rasterdistance.tif"

    R_Raster_Distance = processing.run("gdal:proximity",\
        {'INPUT':R_Raster['OUTPUT'],\
        'BAND':1,\
        'VALUES':'','UNITS':0,'MAX_DISTANCE':0,'REPLACE':0,\
        'NODATA':0,'OPTIONS':'',\
        'DATA_TYPE':5,\
        'OUTPUT':outfile})