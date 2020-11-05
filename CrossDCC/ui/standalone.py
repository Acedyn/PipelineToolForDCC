print("Loading pipeline tools")

import re
import os
import sys

dirname = os.path.dirname(__file__)
reg = re.compile(r"\\[^\\]+$")
dirname = reg.sub("", dirname)
print(dirname)

sys.path.append(r"D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC")        #append DCC lib
sys.path.append(dirname + r"\utils")  #append QT lib
from Qt import QtWidgets, QtCompat

print("Pipeline tools loaded")

from ui import openWindow

app = QtWidgets.QApplication(sys.argv)
win = openWindow.OpenWindow()
win.show()
app.exec_()