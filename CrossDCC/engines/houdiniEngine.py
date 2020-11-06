import hou
import engine
import subprocess
import os
import re

class HoudiniEngine(engine.Engine):
    def open(self, path):
        hou.hipFile.load(path)

    def export(self, path, namespaceString, openFilePath):
        print("Alembic export from houdini not supported yet")
 
    def importAbc(self, importFolderPath, namespaceString, destinationFilePath):
        dirname = os.path.dirname(__file__)
        reg = re.compile(r"\\[^\\]+$")
        dirname = reg.sub("", dirname)
        dirname = dirname.replace("\\", "/")

        if not os.path.isfile(destinationFilePath) :
            houdiniAbcInitQuery = "hython \"" + dirname + "/script/houdiniInitFile.py\" \"" + destinationFilePath + "\""
            print(houdiniAbcInitQuery)
            subprocess.Popen(houdiniAbcInitQuery, shell=True).wait()

        houdiniAbcImportQuery = "hython \"" + destinationFilePath + "\" \"" + dirname + "/script/houdiniAbcImport.py\" \"" + importFolderPath + "\" \"" + namespaceString + "\""
        print(houdiniAbcImportQuery)
        subprocess.Popen(houdiniAbcImportQuery, shell=True)