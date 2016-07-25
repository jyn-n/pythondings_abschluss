#!/bin/python

from core import game
from main_window import main_window
g = game()


app = QtGui.QApplication(sys.argv)
mw = main_window()
mw.show()
sys.exit(app.exec_())

