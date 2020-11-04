import maya.cmds as cmds
import engine
import subprocess

class MayaEngine(engine.Engine):
    def open(self, path):
        cmds.file(path, o=True)
        print(path)
 
    def export(self, path, namespaceString, openFilePath):
        if openFilePath == "" :
            openFilePath = cmds.file(q=True, sn=True)

        path = path.replace("\\", "/")
        openFilePath = openFilePath.replace("\\", "/")

        mayabatch = "D:/Programes/Maya 2020/Maya2020/bin/mayabatch.exe"
        mayaFile = "C:/Users/Simon/Desktop/temp.mb"
        abcExportScript = "D:/Simon/Mes Documents/PROJECT/2020/WS2020_PythonForDCC/CrossDCC/script/mayaAbcExport.py"

        mayaAbcExportQuery = "\"" + mayabatch + "\" -command \"python(\\\"execfile(\'" + abcExportScript + "\')\\\");\" \"" + path + "\" \"" + namespaceString + "\" -file \"" + mayaFile + "\""
        print(mayaAbcExportQuery)
        subprocess.Popen(mayaAbcExportQuery, shell=True)
