import hou
import sys

# Get the argument
initFilePath = sys.argv[1]
# Save the file
hou.hipFile.save(initFilePath)