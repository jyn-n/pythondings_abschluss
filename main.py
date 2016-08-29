#!/bin/python

from core import game
from main_window import main_window
from event import event_manager
from event import logger
from event import log
import core.data.events as events
from PyQt4 import QtGui
import sys

#init objects

l = logger ( log.error, log.warning )
#l = logger ( log.error, log.warning , log.event )
e = event_manager(l)
g = game(e)

#event callback methods
def event_tick():
	mw.update_gamestate(g.tick())

def event_win():
	mw.win()

def event_lose():
	mw.lose()

def load_level( name ):
	g.load_level(name)
	mw.init_gamestate(g)

#register events

r = e.register_event

r ( events.spawn_attacker, g.spawn_attacker )
r ( events.move, g.move )
r ( events.load_level, load_level )
r ( events.place_tower, g.place_tower )
r ( events.spawn_wave, g.spawn_wave )
r ( events.move_all, g.move_all )
r ( events.die, g.die )
r ( events.take_damage, g.take_damage )
r ( events.fire_tower, g.fire_tower )
r ( events.fire_all, g.fire_all )
r ( events.tick, event_tick)
r ( events.lose, event_lose )
r ( events.win, event_win )
r ( events.lose_life, g.lose_life )
r ( events.get_money, g.get_money)
r ( events.lose_money, g.lose_money)

del r

#testing stuff

#e ( events.load_level, "demo_level" )

#create main window
app = QtGui.QApplication(sys.argv)
mw = main_window(event_callback = e, interval = 20)
mw.show()
sys.exit(app.exec_())

