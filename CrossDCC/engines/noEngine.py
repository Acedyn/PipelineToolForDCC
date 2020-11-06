import engine
import os
import subprocess
import os
import re
import time
from pathlib import Path

class NoEngine(engine.Engine):
    def open(self, path):
        query = "PowerShell.exe " + "\"" + 'start ' + "\'" + path + "\'" + "\""
        print(query)
        os.system(query)
        
    def export(self, path, namespaceString, openFilePath):
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

        dirname = os.path.dirname(__file__)
        reg = re.compile(r"\\[^\\]+$")
        dirname = reg.sub("", dirname)
        dirname = dirname.replace("\\", "/")

        path = Path(destinationFilePath)
        if not path.is_file():
            houdiniAbcInitQuery = "hython \"" + dirname + "/script/houdiniInitFile.py\" \"" + destinationFilePath + "\""
            print(houdiniAbcInitQuery)
            subprocess.run(houdiniAbcInitQuery, shell=True)

        houdiniAbcImportQuery = "hython \"" + destinationFilePath + "\" \"" + dirname + "/script/houdiniAbcImport.py\" \"" + importFolderPath + "\" \"" + namespaceString + "\""
        print(houdiniAbcImportQuery)
        subprocess.Popen(houdiniAbcImportQuery, shell=True)