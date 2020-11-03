import maya.cmds as cmds
import engine

class MayaEngine(engine.Engine):
    def open(self, path):
        cmds.file(path, o=True)
        print(path)
 
