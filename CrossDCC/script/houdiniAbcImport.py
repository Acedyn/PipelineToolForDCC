import hou
import sys
import os
import re

importFolderPath = sys.argv[1]
namespaceString = sys.argv[2]

importFolderContent = os.listdir(importFolderPath)

namespaces = namespaceString.split(" ")
for namespace in namespaces :
    geometry = hou.node("/obj").createNode("geo")

    for importFolderFile in importFolderContent :
        reg = re.compile(r"^" + namespace)

        if(reg.match(importFolderFile)):
            alembicRop = geometry.createNode("alembic")
            alembicRop.parm("fileName").set(importFolderFile)


print("IMPORT PATH : " + importFolderPath)
print("NAMESPACE : " + namespaceString)

hou.hipFile.save()


        
        