# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MCDM
                                 A QGIS plugin
 This plugin is provide facilitates to work eith vector and raster files to find a suitable place to establish solar farm in New Mexico, United States
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-02-11
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Prasadi Senadeera
        email                : prasadisenadeera1991@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog
from qgis.gui import *
from qgis.core import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QComboBox
from osgeo import gdal
from osgeo.gdalconst import *





# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .MCDM_dialog import MCDMDialog
from .reclassify import reclassify
import os.path
import processing
import tempfile
import numpy as np
from numpy import array
import os


class MCDM:
    """QGIS Plugin Implementation."""
    def __init__(self, iface):
        """Constructor.
        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MCDM_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Multi Criteria Decision Maker')
        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.
        We implement this ourselves since we do not inherit QObject.
        :param message: String for translation.
        :type message: str, QString
        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('MCDM', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/MCDM/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'MCDM'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Multi Criteria Decision Maker'),
                action)
            self.iface.removeToolBarIcon(action)


    def select_output_file(self):
        filename, _filter = QFileDialog.getSaveFileName(
        self.dlg, "Select output file ","", '*.tif')
        self.dlg.lineEdit.setText(filename)

    #Rasterization tool
    def rasterize(self,infile,Boundary):
        tf = tempfile.TemporaryDirectory()
        tfolder = tf.name + "\\Rasterisation.tif"
        area=Boundary.extent()
        raster=processing.run("gdal:rasterize",        
            {'INPUT':infile,\
            'FIELD':None,'BURN':1,'UNITS':1,\
            'WIDTH':2,'HEIGHT':2,\
            'EXTENT':area,\
            'NODATA':0,'OPTIONS':'','DATA_TYPE':5,'INIT':None,\
            'INVERT':False,\
            'OUTPUT': tfolder})
        rlayer = self.iface.addRasterLayer(tfolder, "Rasterisation")
        return rlayer 
    
    #Raster distance tool
    def Rasterdistance(self,infile):
        tf = tempfile.TemporaryDirectory()
        tfolder = tf.name + "\\Rasterdistance.tif"
        raster_distance=processing.run("gdal:proximity",\
            {'INPUT':infile,\
            'BAND':1,\
            'VALUES':'','UNITS':0,'MAX_DISTANCE':0,'REPLACE':0,\
            'NODATA':0,'OPTIONS':'',\
            'DATA_TYPE':5,\
            'OUTPUT':tfolder})
        rlayer=self.iface.addRasterLayer(tfolder, "Rasterdistance")
        return rlayer
    
    #Raster Clip tool
    def RasterClip(self,infile,cliper):
        tf = tempfile.TemporaryDirectory()
        tfile = tf.name + "\\Rasterclip.tif"
        area=cliper.extent()
        processing.run("gdal:cliprasterbyextent",\
        {'INPUT':infile,\
        'PROJWIN':area,\
        'NODATA':None,'OPTIONS':'',\
        'DATA_TYPE':0,\
        'OUTPUT':tfile})
        rlayer = self.iface.addRasterLayer(tfile, "Rasterclip")
        return rlayer

    
    #Resampling
    def resample (self, infile):
        tf = tempfile.TemporaryDirectory()
        tfile = tf.name + "\\resample.txt"
        processing.run("grass7:r.resample", 
            {'input':infile,\
            'output':tfile,\
            'GRASS_RASTER_FORMAT_OPT':'',\
            'GRASS_RASTER_FORMAT_META':''})
        rlayer = self.iface.addRasterLayer(tfile, "resample")
        return tfile
    
    #Vector Clip 
    def Vectorclip(infile,clipfile):
        tf = tempfile.TemporaryDirectory()
        tfile = tf.name + "\\Vectorclip.txt"
        area=clipfile.extent()
        processing.run("native:extractbyextent", 
            {'INPUT':infile,\
            'EXTENT':area,\
            'CLIP':True,\
            'OUTPUT':tfile})
        rlayer = self.iface.addRasterLayer(tfile, "Vectorclip")
        return rlayer
        

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = MCDMDialog()
            self.dlg.pushButton.clicked.connect(self.select_output_file)
        
        # Fetch the currently loaded layers
        layers = QgsProject.instance().layerTreeRoot().children()
        # Clear the contents of the comboBox and lineedit from previous runs
        self.dlg.mMapLayerComboBox_1.clear()
        self.dlg.lineEdit.clear()
        # Populate the comboBoxes with names of all the loaded layers
        self.dlg.mMapLayerComboBox_1.addItems([layer.name() for layer in layers])
        self.dlg.mMapLayerComboBox_2.addItems([layer.name() for layer in layers])
        self.dlg.mMapLayerComboBox_3.addItems([layer.name() for layer in layers])
        self.dlg.mMapLayerComboBox_4.addItems([layer.name() for layer in layers])
        self.dlg.mMapLayerComboBox_5.addItems([layer.name() for layer in layers])
        self.dlg.mMapLayerComboBox_6.addItems([layer.name() for layer in layers])
        self.dlg.mMapLayerComboBox_7.addItems([layer.name() for layer in layers])
        self.dlg.mMapLayerComboBox.addItems([layer.name() for layer in layers])

# show the dialog
        self.dlg.show()
# Run the dialog event loop
        result = self.dlg.exec_()
# See if OK was pressed
        if result:

#getting the boundary
            Boundary = self.dlg.mMapLayerComboBox.currentText()
            V_Boundary = QgsProject().instance().mapLayersByName(Boundary)[0]

 #getting the browsed file name
            filename = self.dlg.lineEdit.text()

# Road network  
            #Road = self.dlg.mMapLayerComboBox_1.currentText()
            #V_Road = QgsProject().instance().mapLayersByName(Road)[0]

            #R_Road=self.rasterize(V_Road,V_Boundary)
            #R_Road_distance=self.Rasterdistance(R_Road)
            #R_Road_dist_clip=self.RasterClip(R_Road_distance,V_Boundary)
            
            #Reclassify road
            #Road_O = str(self.dlg.comboBox.currentText())
            #RRDC_reclass=self.reclassify(R_Road_dist_clip,Road_O)

# Transmission lines
            #Transmission = self.dlg.mMapLayerComboBox_2.currentText()
            #V_Transmission = QgsProject().instance().mapLayersByName(Transmission)[0]

            #R_Trasmission=self.rasterize(V_Transmission,V_Boundary)
            #R_Transmission_distance=self.Rasterdistance(R_Trasmission)
            #R_Tran_dist_clip=self.RasterClip(R_Transmission_distance,V_Boundary)

            #Reclassify transmission lines
            #Transmission_O = str(self.dlg.comboBox_3.currentText())
            #R_Tran_dist_clip_reclass=self.reclassify(R_Tran_dist_clip,Transmission_O)

# Restrcited Lands
            #Restric_Land = self.dlg.mMapLayerComboBox_3.currentText()
            #V_Restric_Land = QgsProject().instance().mapLayersByName(Restric_Land)[0]

            #R_Restric_Land= self.rasterize(V_Restric_Land,V_Boundary)
            #R_Restric_Land_clip=self.RasterClip(R_Restric_Land,V_Boundary)

# Land Cover

# Population density
            #PopDe = self.dlg.mMapLayerComboBox_5.currentText()
            #V_PopDe = QgsProject().instance().mapLayersByName(PopDe)[0]
            
            #R_PopDe=self.rasterize(V_PopDe)
            #R_Pop_Reclass=self.reclassify(R_PopDe)


# Solar resource potential 
            #Solar = self.dlg.mMapLayerComboBox_6.currentText()
            #V_Solar = QgsProject().instance().mapLayersByName(Solar)[0]
            #V_Solar_Mex= self.Vectorclip(V_Solar,V_Boundary)

            #R_Solar_Mex=self.rasterize(V_Solar_Mex,V_Boundary)


            #Solar_O = str(self.dlg.comboBox_6.currentText())
            #R_Solar_Reclass=self.reclassify(R_Solar,Solar_O)


#City centroids
            City = self.dlg.mMapLayerComboBox_7.currentText()
            V_City = QgsProject().instance().mapLayersByName(City)[0]
            
            City_O = str(self.dlg.comboBox_7.currentText())
            
            
            R_City=self.rasterize(V_City,V_Boundary)
            RCdistance=self.Rasterdistance(R_City)
            RCD_clip=self.RasterClip(RCdistance,V_Boundary)

            RCDC_reclassify=reclassify(RCD_clip,City_O)

            QgsProject.instance().removeAllLayers()
        


        
            

            
            
            
            
            
       
