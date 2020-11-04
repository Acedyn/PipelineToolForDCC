# FOR MAYA add to maya.env   SHELF before SCRIPT is important
# MAYA_SHELF_PATH = %MAYA_SHELF_PATH%;D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\engines\maya\shelves
# MAYA_SCRIPT_PATH = %MAYA_SCRIPT_PATH%;D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\engines\maya\scripts

# FOR HOUDINI add to houdini.env
# HOUDINI_SCRIPT_PATH = "D:/Simon/PROJECT/2020/WS2020_PythonForDCC/CrossDCC/engines/houdini/scripts;&"
# HOUDINI_TOOLBAR_PATH = "D:/Simon/PROJECT/2020/WS2020_PythonForDCC/CrossDCC/engines/houdini/toolbar;&"

import os
import sys

sys.path.append(r"D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\utils")           #append QT lib
from Qt import QtWidgets, QtCompat

ui_path = r"D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\ui\basicsUI.ui"

from engines import engine as dcc

class OpenWindow(QtWidgets.QMainWindow):
    
    engine = dcc.getCurrentDCC()

    def __init__(self):
        super(OpenWindow, self).__init__()
        QtCompat.loadUi(ui_path, self)    
        self.openButton.clicked.connect(self.open)
        self.exportButton.clicked.connect(self.export)
        self.searchOpenButton.clicked.connect(self.searchOpen)
        self.searchExportButton.clicked.connect(self.searchExport)
        
    def open(self):
        openFilePath = self.openPath.text()
        self.engine.open(openFilePath)

    def export(self):
        exportFilePath = self.exportPath.text()
        openFilePath = self.openPath.text()
        namespaceString = self.exportNameSpaces.text()
        self.engine.export(exportFilePath, namespaceString, openFilePath)

    def searchOpen(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", r"C:\Users\Simon\Documents")
        self.openPath.setText(fileName[0])

    def searchExport(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, "Export Folder", r"C:\Users\Simon\Documents")
        self.exportPath.setText(fileName)