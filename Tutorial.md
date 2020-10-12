# Automated Multicriteria Evaluation for Solar Farm Siting Tutorial

This guide explains how to use an experimental QGIS plugin that produces a weighted overlay raster image through automating the preprocessing steps of the variables used in multicriteria evaluation for solar farms.

1. Import data from DropBox at https://www.dropbox.com/transfer/AAAAALd-TeEefdxwd2_DO0bEIvc3TnjAz8WHjIWXqD0Tgawz9eI_qFE

2. Import experimental plug-in zipfile from 'zipfiles' folder named 'qgisplugin.zip'

3. Open QGIS3 with GRASS 7.6

4. Import data layers to layer pane of QGIS using the data zipfile.

5. In the plugins menu, go to 'Manage and install plugins...'

- Click 'Install from zip' and import the experimental plugin

- Once imported click 'Install Plugin'

6. In the same window, go to 'Install plugins' and check the box next to 'Multi Criteria Decision Maker'

- Click 'Close'

7. The experimental button should appear in the toolbar of QGIS.

- Click the on the button

8. Import files in the correct places, fill in suitability rank and relative weight, pixel size = 0 and output location.

  ![Figure 1](/images/scoresweights.PNG "Scores and Weights")

- Click 'Ok'

9. Output raster will appear in the layer pane
