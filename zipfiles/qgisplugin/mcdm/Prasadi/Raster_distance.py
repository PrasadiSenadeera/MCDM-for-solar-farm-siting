
import processing


def Raster_Distance(infile,outfile)
    processing.run("gdal:proximity", \
        {'INPUT':infile,'BAND':1,\
        'VALUES':'','UNITS':0,'MAX_DISTANCE':0,'REPLACE':0,\
        'NODATA':0,'OPTIONS':'',\
        'DATA_TYPE':5,\
        'OUTPUT':output})