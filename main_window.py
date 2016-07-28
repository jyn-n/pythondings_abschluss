from PyQt4 import QtCore, QtGui, uic
import functools

import core.data.events as events

ui_main_window, window_base_class = uic.loadUiType("main_window.ui") #TODO make path relative to own directory

class main_window ( window_base_class, ui_main_window ):
	def __init__ (self, parent = None, event_callback = None, gamestate = None, interval = 20):
		window_base_class.__init__(self, parent)
		ui_main_window.__init__(self)
		self.setupUi(self)

		self.set_event_callback (event_callback)
		if gamestate != None:
			self.init_gamestate(gamestate)

		self._timer = QtCore.QTimer()
		self._timer.start(interval)
		self._timer.timeout.connect ( functools.partial (self._event, events.tick) )

	def set_event_callback (self, callback):
		self._event = callback

	def init_gamestate (self, gamestate):
		self.board.update_gamestate(gamestate)

		for tower in gamestate.towers:
			self.list_towers.addItem (tower)

	def update_gamestate (self, gamestate):
		self.board.update_gamestate(gamestate)
		self.repaint()

	def game_board_clicked (self, position):
		self._event ( events.place_tower , str ( self.list_towers.currentItem().text() ) , (position.x(), position.y()) ) 
