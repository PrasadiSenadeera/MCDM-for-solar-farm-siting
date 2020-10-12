 '''
            
            #Taking Reclassified Layers

            Road = self.dlg.mMapLayerComboBox_1.currentText()
            R_Road = QgsProject().instance().mapLayersByName(Road)[0] 
            
            Transmission = self.dlg.mMapLayerComboBox_2.currentText()
            R_Transmission = QgsProject().instance().mapLayersByName(Transmission)[0]

            Restricted= self.dlg.mMapLayerComboBox_3.currentText()
            R_Restricted = QgsProject().instance().mapLayersByName(Restricted)[0]

            LandC= self.dlg.mMapLayerComboBox_4.currentText()
            R_LandCo= QgsProject().instance().mapLayersByName(LandC)[0] 

            PopDe= self.dlg.mMapLayerComboBox_5.currentText()
            R_PopDe= QgsProject().instance().mapLayersByName(PopDe)[0] 

            Solar= self.dlg.mMapLayerComboBox_6.currentText()
            R_Solar= QgsProject().instance().mapLayersByName(Solar)[0]

            CityCe= self.dlg.mMapLayerComboBox_7.currentText()
            R_CityCe= QgsProject().instance().mapLayersByName(CityCe)[0] 

            #Getting Weights

            Road_W =int(self.dlg.spinBox.value())
            Transmis_W =int(self.dlg.spinBox_2.value())
            LandC_W =int(self.dlg.spinBox_4.value())
            PopDe_W =int(self.dlg.spinBox_5.value())
            Solar_W =int(self.dlg.spinBox_6.value())
            City_W =int(self.dlg.spinBox_7.value())

            a=[R_Road,R_Transmission,R_LandCo,R_PopDe,R_Solar,R_CityCe]
            b=[Road_W,Transmis_W,LandC_W,PopDe_W,Solar_W,City_W]

            A_Road=self.layerAsArray(R_Road)
            A_Transmission=self.layerAsArray(R_Transmission)
            A_LandCo=self.layerAsArray(R_LandCo)
            A_PopDe=self.layerAsArray(R_PopDe)
            A_Solar=self.layerAsArray(R_Solar)
            A_CityCe=self.layerAsArray(R_CityCe)
            A_Restrict=self.layerAsArray(R_Restricted)

            Total_weight=(Road_W+Transmis_W+LandC_W+PopDe_W+Solar_W+City_W)

            A_Final=(Road_W*A_Road+Transmis_W*A_Transmission+LandC_W*A_LandCo+PopDe_W*A_PopDe+\
                A_Solar*Solar_W+City_W*A_CityCe)/Total_weight

            #Remove restricted Lands from weighted overlay

            rows = A_Final.shape[0]
            cols = A_Final.shape[1]
            Final = np.zeros(shape=(rows,cols))
            for x in range(0, rows):
                for y in range(0, cols):
                    if A_Restrict[x,y]==1:
                        Final[x,y]=0
                    else:
                        Final[x,y]=A_Final[x,y]


            #new file for write output

            driver = gdal.GetDriverByName("GTiff")
            gdal_R_Road = gdal.Open(R_Road.source())
            
            Pix=R_Road.rasterUnitsPerPixelX
            Pix2=R_Road.rasterUnitsPerPixelY
            e = R_Road.extent()
            Xmin=e.xMinimum()        
            Ymin=e.yMinimum()

            
            file2 = driver.Create(filename, R_Road.width(),R_Road.height() ,1)
            file2.SetGeoTransform(gdal_R_Road.GetGeoTransform())
            spatial_reference = osr.SpatialReference()
            spatial_reference.ImportFromEPSG(4151)
            file2.SetProjection(spatial_reference.ExportToWkt())
            file2.GetRasterBand(1).WriteArray(A_Final)
        
            
            
            newLayer = QgsRasterLayer(filename,"Final")
            QgsProject.instance().addMapLayer(newLayer)


            #file2.SetGeoTransform([Xmin, Pix, 0, Ymin, 0, Pix2]
            #newLayer = QgsRasterLayer("rsum.tif","rsum")
            #QgsProject.instance().addMapLayer(newLayer)
            

            self.iface.messageBar().pushMessage("Success", "Output file written at " + filename,
            level=Qgis.Success, duration=3)
            
#https://gis.stackexchange.com/questions/290776/how-to-create-a-tiff-file-using-gdal-from-a-numpy-array-and-specifying-nodata-va
            

            '''