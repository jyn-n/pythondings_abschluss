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
r ( events.fire_tower, g.fire_tower)
r ( events.fire_all, g.fire_all)
r ( events.tick, g.tick)
r ( events.loose)
r ( events.win)
r (events.loose_life, g.loose_life)

del r

#testing stuff

e ( events.load_level, "data/levels/1.yaml" )
e ( events.spawn_attacker, "Goblin", (0,0))
e ( events.place_tower, "Laser Tower", (1,0))
e (events.fire_all)
print(g.attackers[0].get_hp())

#create main window
"""
app = QtGui.QApplication(sys.argv)
mw = main_window(event_callback = e, gamestate = g)
mw.show()
mw.board.update_gamestate (g)
sys.exit(app.exec_())
"""
