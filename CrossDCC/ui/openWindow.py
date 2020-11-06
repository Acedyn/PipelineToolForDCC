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

# Get the path to the current file for relative path
dirname = os.getcwd()
reg = re.compile(r"\\[^\\]+$")
dirname = reg.sub("", dirname)
dirname = dirname.replace("\\", "/")

# Import the QT lib
sys.path.append(dirname)
from Qt import QtWidgets, QtCompat

# Path to the UI
ui_path = dirname + r"\ui\basicsUI.ui"

# Import the engine library containing the DCC related functions
from engines import engine as dcc


class OpenWindow(QtWidgets.QMainWindow):
    
    # Set the engine according to where the tool is launched from
    engine = dcc.getCurrentDCC()

    def __init__(self):
        super(OpenWindow, self).__init__()
        QtCompat.loadUi(ui_path, self)

        # Assign the buttons to functions
        self.exportButton.clicked.connect(self.exportAbc)
        self.importButton.clicked.connect(self.importAbc)
        self.searchOpenFileButton.clicked.connect(self.searchOpenFile)
        self.searchExportFolderButton.clicked.connect(self.searchExportFolder)
        self.searchExportFileButton.clicked.connect(self.searchExportFile)
        self.searchOpenFolderButton.clicked.connect(self.searchOpenFolder)
        
    # Open the file at openFilePath
    def open(self):
        openFilePath = self.openFilePath.text()
        self.engine.open(openFilePath)

    # Export the objects matching the namespaces from the file in openFilePath to the folder at the openFilePath
    def exportAbc(self):
        # Get all the path
        exportFilePath = self.exportFolderPath.text()
        openFilePath = self.openFilePath.text()
        namespaceString = self.exportNameSpaces.text()
        # Call the exportAbc function of the engine
        self.engine.export(exportFilePath, namespaceString, openFilePath)
        
    # Import the .abc matching the namespaces from the folder in importFolderPath to the file at the openFolderPath
    def importAbc(self):
        # Get all the path
        openFolderPath = self.openFolderPath.text()
        exportFilePath = self.exportFilePath.text()
        namespaceString = self.exportNameSpaces.text()
        # Call the importAbc function of the engine
        self.engine.importAbc(openFolderPath, namespaceString, exportFilePath)

    # Open a file dialog window to set openFilePath
    def searchOpenFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
        self.openFilePath.setText(fileName[0])

    # Open a folder dialog window to set exportFolderPath
    def searchExportFolder(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, "Export Folder")
        self.exportFolderPath.setText(fileName)

    # Open a file dialog window to set exportFilePath
    def searchExportFile(self):
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, "Output file")
        self.exportFilePath.setText(filePath[0])
        
    # Open a folder dialog window to set openFolderPath
    def searchOpenFolder(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory(self, "Input folder")
        self.openFolderPath.setText(folderPath)