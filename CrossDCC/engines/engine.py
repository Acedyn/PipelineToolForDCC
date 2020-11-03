import sys
sys.path.append(r"D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\engines")

class Engine():
    def open(self, path):
        print("No DCC detected")
        pass
    
    def save(self, path):
        print("No DCC detected")
        pass
    
def getCurrentDCC():

    engine = Engine()

    if "maya" in sys.executable:
        import mayaEngine
        engine = mayaEngine.MayaEngine()

    elif "houdini" in sys.executable:
        import houdiniEngine
        engine = houdiniEngine.HoudiniEngine()

    else:
        import noEngine
        engine = noEngine.NoEngine()
    
    return engine