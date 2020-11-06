import re
import os
import sys

# Get the path to the current file for relative path
dirname = os.getcwd()
reg = re.compile(r"\\[^\\]+$")
dirname = reg.sub("", dirname)
dirname = dirname.replace("\\", "/")

# Import pipeline module
sys.path.append(dirname)
from Qt import QtWidgets, QtCompat
from ui import openWindow

# Create the app (required only for stand alone)
app = QtWidgets.QApplication(sys.argv)

# Create window instance and show it
win = openWindow.OpenWindow()
win.show()
app.exec_()