import sys
import maya.cmds as cmds

# Load the abc plugin
cmds.loadPlugin( 'AbcExport.mll' )
cmds.loadPlugin( 'AbcImport.mll' )

# Get the arguments
path = sys.argv[3]
namespaceString = sys.argv[4]

path = "\"" + path

# For each namespaces
namespaces = namespaceString.split(" ")
for namespace in namespaces :

    # Find the object matching the namespace
    searchString = namespace + ":*"
    matchObjects = cmds.ls(searchString, transforms=True)

    # For each objects that matches the namespace
    for matchObject in matchObjects :
        # Rename the object because for some reason the caracter ":" doesn't work
        exportName = matchObject.replace(namespace + ":", namespace + "_")

        # If the user put the "\" at the end of the path keep it like that
        if path[-1] == "\\" :
            abcCommand = "-frameRange 1 120 -uvWrite -dataFormat ogawa -root " + matchObject + " -file " + path + exportName + ".abc"
        # if not, add it
        else:
            abcCommand = "-frameRange 1 120 -uvWrite -dataFormat ogawa -root " + matchObject + " -file " + path + "/" + exportName + ".abc"
                
        abcCommand = abcCommand + "\""
        # Send abc command to maya
        cmds.AbcExport(j=abcCommand)
