import engine
import os
import subprocess

class NoEngine(engine.Engine):
    def open(self, path):
        query = "PowerShell.exe " + "\"" + 'start ' + "\'" + path + "\'" + "\""
        print(query)
        os.system(query)
        
    def export(self, path, namespaceString, openFilePath):
        path = path.replace("\\", "/")
        openFilePath = openFilePath.replace("\\", "/")

        mayabatch = "D:/Programes/Maya 2020/Maya2020/bin/mayabatch.exe"
        abcExportScript = "D:/Simon/Mes Documents/PROJECT/2020/WS2020_PythonForDCC/CrossDCC/script/mayaAbcExport.py"

        mayaAbcExportQuery = "\"" + mayabatch + "\" -command \"python(\\\"execfile(\'" + abcExportScript + "\')\\\");\" \"" + path + "\" \"" + namespaceString + "\" -file \"" + openFilePath + "\""
        print(mayaAbcExportQuery)
        subprocess.Popen(mayaAbcExportQuery, shell=True)
