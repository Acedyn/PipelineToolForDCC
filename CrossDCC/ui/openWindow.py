# FOR MAYA add to maya.env   SHELF before SCRIPT is important
# MAYA_SHELF_PATH = %MAYA_SHELF_PATH%;D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\engines\maya\shelves
# MAYA_SCRIPT_PATH = %MAYA_SCRIPT_PATH%;D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\engines\maya\scripts

# FOR HOUDINI add to houdini.env
# HOUDINI_SCRIPT_PATH = "D:/Simon/PROJECT/2020/WS2020_PythonForDCC/CrossDCC/engines/houdini/scripts;&"
# HOUDINI_TOOLBAR_PATH = "D:/Simon/PROJECT/2020/WS2020_PythonForDCC/CrossDCC/engines/houdini/toolbar;&"

# Make sure to have an environment variable with the path to mayabatch.exe (maya)
# Make sure to have an environment variable with the path to hcmd.exe (houdini)

import os
import sys
import re

dirname = os.path.dirname(__file__)
reg = re.compile(r"\\[^\\]+$")
dirname = reg.sub("", dirname)

sys.path.append(dirname + r"\utils")           #append QT lib
from Qt import QtWidgets, QtCompat

ui_path = dirname + r"\ui\basicsUI.ui"

from engines import engine as dcc

class OpenWindow(QtWidgets.QMainWindow):
    
    engine = dcc.getCurrentDCC()

    def __init__(self):
        super(OpenWindow, self).__init__()
        QtCompat.loadUi(ui_path, self)    
        self.openButton.clicked.connect(self.open)
        self.exportButton.clicked.connect(self.export)
        self.importButton.clicked.connect(self.importAbc)
        self.searchOpenButton.clicked.connect(self.searchOpen)
        self.searchExportButton.clicked.connect(self.searchExport)
        self.searchExportFileButton.clicked.connect(self.searchExportFile)
        self.searchOpenFolderButton.clicked.connect(self.searchOpenFolder)
        
    def open(self):
        openFilePath = self.openPath.text()
        self.engine.open(openFilePath)

    def export(self):
        exportFilePath = self.exportPath.text()
        openFilePath = self.openPath.text()
        namespaceString = self.exportNameSpaces.text()
        self.engine.export(exportFilePath, namespaceString, openFilePath)
        
    def importAbc(self):
        importFolderPath = self.openFolderPath.text()
        destinationFilePath = self.exportFilePath.text()
        namespaceString = self.exportNameSpaces.text()
        self.engine.importAbc(importFolderPath, namespaceString, destinationFilePath)

    def searchOpen(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
        self.openPath.setText(fileName[0])

    def searchExport(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, "Export Folder")
        self.exportPath.setText(fileName)

    def searchExportFile(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Output file")
        self.exportFilePath.setText(filePath[0])
        
    def searchOpenFolder(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, "Input folder")
        self.openFolderPath.setText(folderPath)