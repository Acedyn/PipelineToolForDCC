import maya.cmds as cmds
import engine
import subprocess
import os
import re

class MayaEngine(engine.Engine):
    def open(self, path):
        cmds.file(path, o=True)
        print(path)
 
    def export(self, path, namespaceString, openFilePath):
        # If no openFilePath is given -> use the current maya file opened
        if openFilePath == "" :
            openFilePath = cmds.file(q=True, sn=True)

        # Set the path to have forward slashes
        path = path.replace("\\", "/")
        openFilePath = openFilePath.replace("\\", "/")

        # Get the path to the current file for relative path
        dirname = os.path.dirname(__file__)
        reg = re.compile(r"\\[^\\]+$")
        dirname = reg.sub("", dirname)
        dirname = dirname.replace("\\", "/")
        
        # Path to the script for alembic export
        abcExportScript = dirname + "/script/mayaAbcExport.py"

        # Command to use script for alembic export on the given .ma file, passing the namespaceString and openFilePath as argument
        mayaAbcExportQuery = "mayabatch -command \"python(\\\"execfile(\'" + abcExportScript + "\')\\\");\" \"" + path + "\" \"" + namespaceString + "\" -file \"" + openFilePath + "\""
        subprocess.Popen(mayaAbcExportQuery, shell=True)

    def importAbc(self, importFolderPath, namespaceString, destinationFilePath):
        print("Alembic import to houdini not supported yet")