# CROSS DCC tool
### Prerequisite :
- Set the path environment variables with the path to mayabatch.exe (maya) and hcmd.exe (houdini)
- FOR MAYA add to maya.env   SHELF before SCRIPT is important : 
    - MAYA_SHELF_PATH = %MAYA_SHELF_PATH%;path/to/CrossDCC/engines/maya/shelves
    - MAYA_SCRIPT_PATH = %MAYA_SCRIPT_PATH%;path/to/CrossDCC/engines/maya/scripts
- FOR HOUDINI add to houdini.env
    - HOUDINI_SCRIPT_PATH = "path/to/CrossDCC/engines/houdini/scripts;&"
    - HOUDINI_TOOLBAR_PATH = path/to/CrossDCC/engines/houdini/toolbar;&"