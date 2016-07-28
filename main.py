#!/bin/python

from core import game
from main_window import main_window
from event import event_manager
from PyQt4 import QtGui
import sys

#init objects

e = event_manager()
g = game(e)

#register events

#testing stuff

g.load_level ("data/levels/1.yaml")

#create main window

app = QtGui.QApplication(sys.argv)
mw = main_window()
mw.show()
mw.init_game(g)
mw.board.update_gamestate (g)
sys.exit(app.exec_())

