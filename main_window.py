from PyQt4 import QtCore, QtGui, uic

ui_main_window, window_base_class = uic.loadUiType("main_window.ui") #TODO make path relative to own directory

class main_window ( window_base_class, ui_main_window ):
	def __init__ (self, parent = None):
		window_base_class.__init__(self, parent)
		ui_main_window.__init__(self)
		self.setupUi(self)

	def init_game (self, game ):
		self._game = game
		for t in game.attacker_type:
			self.list_attacker_types.addItem (t)
		self.list_attacker_types.setCurrentRow(0)

	def select_attacker_type (self, row):
		t = str(self.list_attacker_types.item(row).text())
		self.label_attacker_type_name.setText ( self._game.attacker_type[t].name )
		self.label_attacker_type_speed.setText ( str (self._game.attacker_type[t].speed ) )
		self.label_attacker_type_money.setText ( str (self._game.attacker_type[t].money ) )
		self.label_attacker_type_hp.setText ( str (self._game.attacker_type[t].hp ) )

