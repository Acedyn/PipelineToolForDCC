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
        # Set the path to have forward slashes
        importFolderPath = importFolderPath.replace("\\", "/")
        destinationFilePath = destinationFilePath.replace("\\", "/")
        
        # Get the path to the current file for relative path
        dirname = os.path.dirname(__file__)
        reg = re.compile(r"\\[^\\]+$")
        dirname = reg.sub("", dirname)
        dirname = dirname.replace("\\", "/")

        # If the file we want to import the alembic into doesn't exist -> create it
        if not os.path.isfile(destinationFilePath) :
            # Command to call script that create the .hip file, passing its desination as argument
            houdiniAbcInitQuery = "hython \"" + dirname + "/script/houdiniInitFile.py\" \"" + destinationFilePath + "\""
            subprocess.Popen(houdiniAbcInitQuery, shell=True).wait()

        # Command to call script that import the alembic files in the .hip, passing the namespaceString and importFolderPath as argument
        houdiniAbcImportQuery = "hython \"" + destinationFilePath + "\" \"" + dirname + "/script/houdiniAbcImport.py\" \"" + importFolderPath + "\" \"" + namespaceString + "\""
        subprocess.Popen(houdiniAbcImportQuery, shell=True)