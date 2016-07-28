from PyQt4 import QtCore, QtGui, uic

ui_main_window, window_base_class = uic.loadUiType("main_window.ui") #TODO make path relative to own directory

class main_window ( window_base_class, ui_main_window ):
	def __init__ (self, parent = None, event_callback = None, gamestate = None):
		window_base_class.__init__(self, parent)
		ui_main_window.__init__(self)
		self.setupUi(self)

		self.set_event_callback (event_callback)
		if gamestate != None:
			self.init_gamestate(gamestate)

	def set_event_callback (self, callback):
		self.event = callback
		self.board.set_event_callback (self, callback)

	def init_gamestate (self, gamestate):
		for tower in gamestate.towers:
			self.list_towers.addItem (tower)
