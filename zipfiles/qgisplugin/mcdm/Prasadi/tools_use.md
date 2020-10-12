
# Electric Power Lines and Road Network

####	Euclidean Distance
Three seperate steps should be followed for the tool, 1. Rasterizartion 2. Raster Distance 3.Clip raster by extent
1. Rasterization tool— (tool can be found at: raster-conversion- rasterize)

##### variables to feed:
* Input layer: G:\GISA-Project\OLD\Data\TR_Transport_Li.shp
* A fixed value to burn: 1
* output raster size unit: Georeferenced units
* Width/ Horizontal Resolution: 25
* Height/Vertical Resolution:25
* Processing extent: Area.shp
* Output layer: E:/NOVA/Project/test/Road_raster.tif


```Bash
processing.run("gdal:rasterize", {'INPUT':'G:\\GISA-Project\\OLD\\Data\\TR_Transport_Li.shp','FIELD':None,'BURN':1,'UNITS':1,'WIDTH':25,'HEIGHT':25,'EXTENT':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]','NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,'INVERT':False,'OUTPUT':'E:/NOVA/Project/test/Road_raster.tif'})
```

2.	Rater Distance (tool can be found at: Raster—analysis—Raster Distance)
##### variables to feed:
* Input layer: E:/NOVA/Project/test/Road_raster.tif
* Distance units; Georeferenced coordinates
* Proximity map: E:/NOVA/Project/test/Raster_Distance.tif

```Bash
processing.run("gdal:proximity", {'INPUT':'E:/NOVA/Project/test/Road_raster.tif','BAND':1,'VALUES':'','UNITS':0,'MAX_DISTANCE':0,'REPLACE':0,'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'OUTPUT':'E:/NOVA/Project/test/Raster_Distance.tif'})
```
3. 	Clip raster by extent
##### variables to feed:
* Input layer: : E:/NOVA/Project/test/Raster_Distance.tif
* Clipping extent: Area.shp
* Clipped: 'E:/NOVA/Project/test/Road_raster_area.tif'
```Bash
processing.run("gdal:cliprasterbyextent", {'INPUT':'E:/NOVA/Project/test/Raster_Distance.tif','PROJWIN':'199647.82427947974,204681.98441158095,164429.30559307119,176876.01571690888 [USER:100000]','NODATA':None,'OPTIONS':'','DATA_TYPE':0,'OUTPUT':'E:/NOVA/Project/test/Road_raster_area.tif'})
```

# Population Density

1. Rasterization tool— (Discussed above)

# Landcover
1. Clip raster by extent

* Input:
* Clipping Extent: 
* ClippedE:/NOVA/Project/test/LandCover_Mexico.tif

```Bash
processing.run("gdal:cliprasterbyextent", {'INPUT':'E:/NOVA/Project/Project_Seminar_Variables/NM_LandCover/NM_CroplandData2018.tif/cdl_30m_r_nm_2018_utm13.tif','PROJWIN':'-109.050173,-103.001964,31.332172,37.000293 [EPSG:4269]','NODATA':None,'OPTIONS':'','DATA_TYPE':0,'OUTPUT':'E:/NOVA/Project/test/LandCover_Mexico.tif'})
```


2. Select by attribute

# City centroids

1. 

# Restricted lands

1. Merge
* Input layers: All layes as user consent
* Destination CRS: Desired Final coordinate system
* Merged: E:/NOVA/Project/test/Restricted_Lands.shp

```Bash
processing.run("native:mergevectorlayers", {'LAYERS':['E:/NOVA/Project/Project_Seminar_Variables/NM_FederalLands/NM_StateParks/NM_StateParks.shp/NMStateParks.shp','E:/NOVA/Project/Project_Seminar_Variables/NM_FederalLands/NM_FederalLands/NM_FederalLands.shp/nm_fedlands_08.shp','E:/NOVA/Project/Project_Seminar_Variables/NM_FederalLands/NM_NationalParks/NM_NationalParks.shp/nm_nps_boundary123119.shp','E:/NOVA/Project/Project_Seminar_Variables/NM_FederalLands/NM_IndianReservations/NM_IndianReservations.shp/tl_2015_us_aiannh.shp'],'CRS':QgsCoordinateReferenceSystem('EPSG:4269'),'OUTPUT':'E:/NOVA/Project/test/Restricted_Lands.shp'})
```

2. Extract/ Clip by extent
 
* Input Layer: Merged.shp
* Extent: New Mexico boundary.shp
* Enable clip features to extent
* Clipped: E:/NOVA/Project/test/Restricted_Lands_mexico.shp

```Bash
processing.run("native:extractbyextent", {'INPUT':'E:\\NOVA\\Project\\test\\Restricted_Lands.shp','EXTENT':'-109.0500967990565,-103.002173,31.332205825166476,37.000152 [EPSG:4269]','CLIP':True,'OUTPUT':'E:/NOVA/Project/test/Restricted_Lands_Mexico.shp'})
```
rlayer.extent().toString()


http://www.qgistutorials.com/en/docs/3/building_a_python_plugin.html
https://medium.com/@abesingh1/writing-qgis-plugin-using-python-3-a-beginners-guide-ddf0be7e5357
https://docs.qgis.org/3.4/en/docs/pyqgis_developer_cookbook/raster.html
https://stackoverflow.com/questions/56038742/creating-in-memory-qgsrasterlayer-from-the-rasterization-of-a-qgsvectorlayer-wit


