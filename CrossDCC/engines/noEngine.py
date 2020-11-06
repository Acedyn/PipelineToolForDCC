import engine
import os
import subprocess
import os
import re

class NoEngine(engine.Engine):
    def open(self, path):
        query = "PowerShell.exe " + "\"" + 'start ' + "\'" + path + "\'" + "\""
        print(query)
        os.system(query)
        
    def export(self, path, namespaceString, openFilePath):
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