import hou
import engine

class HoudiniEngine(engine.Engine):
    def open(self, path):
        hou.hipFile.load(path)

    def export(self, path, namespaceString):
        namespaces = namespaceString.split(" ")
        for namespace in namespaces :
            print("Exporting " + namespace)
        print("Alembic export from houdini not supported yet")
 
