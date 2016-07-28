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

#create ticking method
def tick():
	mw.board.update_gamestate(g.tick())
	mw.repaint()

#register events

r = e.register_event

r ( events.spawn_attacker, g.spawn_attacker )
r ( events.move, g.move )
r ( events.load_level, g.load_level )
r ( events.place_tower, g.place_tower )
r ( events.spawn_wave, g.spawn_wave )
r ( events.move_all, g.move_all )
r ( events.die, g.die )
r ( events.take_damage, g.take_damage )
r ( events.fire_tower, g.fire_tower )
r ( events.fire_all, g.fire_all )
r ( events.tick, tick)
r ( events.loose, lambda: None)
r ( events.win, lambda: None)
r (events.loose_life, g.loose_life)

del r

#testing stuff

e ( events.load_level, "data/levels/1.yaml" )

#create main window
app = QtGui.QApplication(sys.argv)
mw = main_window(event_callback = e, gamestate = g, interval = 20)
mw.show()
e(events.tick)
sys.exit(app.exec_())

