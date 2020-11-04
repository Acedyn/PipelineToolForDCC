import maya.cmds as cmds
import engine

class MayaEngine(engine.Engine):
    def open(self, path):
        cmds.file(path, o=True)
        print(path)
 
    def export(self, path, namespaceString, openFilePath):
        path = "\"" + path
        path = path.replace("\\", "/")

        namespaces = namespaceString.split(" ")
        for namespace in namespaces :
            print("Exporting " + namespace + " namespace")

            searchString = namespace + ":*"
            matchObjects = cmds.ls(searchString, transforms=True)

            for matchObject in matchObjects :
                exportName = matchObject.replace(namespace + ":", namespace + "_")
                print("Exporting " + matchObject + " object")

                if path[-1] == "\\" :
                    abcCommand = "-frameRange 1 120 -uvWrite -dataFormat ogawa -root " + matchObject + " -file " + path + exportName + ".abc"
                else:
                    abcCommand = "-frameRange 1 120 -uvWrite -dataFormat ogawa -root " + matchObject + " -file " + path + "/" + exportName + ".abc"
                
                abcCommand = abcCommand + "\""

                cmds.AbcExport(j=abcCommand)
