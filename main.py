#!/bin/python

from core import game
g = game()

import os
os.chdir ("gui")
from gui import main_window

app = QtGui.QApplication(sys.argv)
mw = main_window()
mw.show()
sys.exit(app.exec_())

