import hou
import sys
import os
import re

# Get the arguments
importFolderPath = sys.argv[1]
namespaceString = sys.argv[2]

# Get all the files in importFolderPath
importFolderContent = os.listdir(importFolderPath)

# For each namespace
namespaces = namespaceString.split(" ")
for namespace in namespaces :
    # Create a geometry node
    geometry = hou.node("/obj").createNode("geo")

    # For each files in importFolderPath
    for importFolderFile in importFolderContent :
        reg = re.compile(r"^" + namespace)

        # If the file name matches the name
        if(reg.match(importFolderFile)):
            #Create the alembic rop and set its path to the file
            alembicRop = geometry.createNode("alembic")
            alembicRop.parm("fileName").set(importFolderFile)

hou.hipFile.save()


        
        