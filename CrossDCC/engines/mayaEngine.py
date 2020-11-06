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
        if openFilePath == "" :
            openFilePath = cmds.file(q=True, sn=True)

        path = path.replace("\\", "/")
        openFilePath = openFilePath.replace("\\", "/")

        dirname = os.path.dirname(__file__)
        reg = re.compile(r"\\[^\\]+$")
        dirname = reg.sub("", dirname)
        dirname = dirname.replace("\\", "/")
        
        abcExportScript = dirname + "/script/mayaAbcExport.py"

        mayaAbcExportQuery = "mayabatch -command \"python(\\\"execfile(\'" + abcExportScript + "\')\\\");\" \"" + path + "\" \"" + namespaceString + "\" -file \"" + openFilePath + "\""
        print(mayaAbcExportQuery)
        subprocess.Popen(mayaAbcExportQuery, shell=True)

    def importAbc(self, importFolderPath, namespaceString, destinationFilePath):
        print("Alembic import to houdini not supported yet")