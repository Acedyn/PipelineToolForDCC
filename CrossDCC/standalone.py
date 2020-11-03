print("Loading pipeline tools")

import sys
sys.path.append(r"D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC")        #append DCC lib
sys.path.append(r"D:\Simon\Mes Documents\PROJECT\2020\WS2020_PythonForDCC\CrossDCC\utils")  #append QT lib
from Qt import QtWidgets, QtCompat

print("Pipeline tools loaded")

from ui import openWindow

app = QtWidgets.QApplication(sys.argv)
win = openWindow.OpenWindow()
win.show()
app.exec_()