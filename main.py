#!/bin/python

from core import game
from main_window import main_window
from event import event_manager
import core.data.events as events
from PyQt4 import QtGui
import sys

#init objects

e = event_manager()
g = game(e)

#register events

r = e.register_event

r ( events.spawn_attacker, g.spawn_attacker )
r ( events.move, g.move )
r ( events.load_level, g.load_level )
r ( events.place_tower, g.place_tower )
r ( events.spawn_wave, g.spawn_wave )
r ( events.move_all, g.move_all )
r ( events.die, g.die)
r ( events.take_damage, g.take_damage)

del r

#testing stuff

e ( events.load_level, "data/levels/1.yaml" )

#create main window

app = QtGui.QApplication(sys.argv)
mw = main_window()
mw.show()
mw.board.update_gamestate (g)
sys.exit(app.exec_())

