import sys
import maya.cmds as cmds

cmds.loadPlugin( 'AbcExport.mll' )
cmds.loadPlugin( 'AbcImport.mll' )

path = sys.argv[3]
namespaceString = sys.argv[4]

path = "\"" + path

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
