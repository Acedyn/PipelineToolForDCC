import os
import sys
import re

dirname = os.path.dirname(__file__)
reg = re.compile(r"\\[^\\]+$")
dirname = reg.sub("", dirname)

sys.path.append(dirname + r"\engines")

class Engine():
    def open(self, path):
        print("No DCC detected")

    def export(self, path, namespaceString, openFilePath):
        print("No DCC detected")

    def importAbc(self, importFolderPath, namespaceString, destinationFilePath):
        print("No DCC detected")
    
    
def getCurrentDCC():

    engine = Engine()

    if "maya" in sys.executable :
        import mayaEngine
        engine = mayaEngine.MayaEngine()

    elif "houdini" in sys.executable :
        import houdiniEngine
        engine = houdiniEngine.HoudiniEngine()

    else :
        import noEngine
        engine = noEngine.NoEngine()
    
    return engine