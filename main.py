#!/bin/python

from core import game
from main_window import main_window
from PyQt4 import QtGui
import sys

g = game()
g.load_level("data/levels/1.yaml")

app = QtGui.QApplication(sys.argv)
mw = main_window()
mw.show()
mw.board.update_gamestate (g)
sys.exit(app.exec_())

