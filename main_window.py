from PyQt4 import QtCore, QtGui, uic

ui_main_window, window_base_class = uic.loadUiType("main_window.ui") #TODO make path relative to own directory

class main_window ( window_base_class, ui_main_window ):
	def __init__ (self, parent = None):
		window_base_class.__init__(self, parent)
		ui_main_window.__init__(self)
		self.setupUi(self)
