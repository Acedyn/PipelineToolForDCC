import hou
import engine

class HoudiniEngine(engine.Engine):
    def open(self, path):
        hou.hipFile.load(path)
 
