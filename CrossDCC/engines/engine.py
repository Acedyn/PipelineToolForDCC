import os
import sys
import re

# Get the path to the current file for relative path
dirname = os.getcwd()
reg = re.compile(r"\\[^\\]+$")
dirname = reg.sub("", dirname)
dirname = dirname.replace("\\", "/")

sys.path.append(dirname + r"\engines")

# Interface class that all engine classes will inherit from
class Engine():
    def open(self, path):
        print("No DCC detected")

    def export(self, path, namespaceString, openFilePath):
        print("No DCC detected")

    def importAbc(self, importFolderPath, namespaceString, destinationFilePath):
        print("No DCC detected")
    
    
# Get where python is launched from and set the good engine instance
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