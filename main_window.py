from PyQt4 import QtCore, QtGui, uic

ui_main_window, window_base_class = uic.loadUiType("main_window.ui") #TODO make path relative to own directory

class main_window ( window_base_class, ui_main_window ):
	def __init__ (self, parent = None):
		window_base_class.__init__(self, parent)
		ui_main_window.__init__(self)
		self.setupUi(self)

#if __name__ == "__main__":
#	mw.board.update_board ({ (x,y) : x % 2 + 2 * (y % 2) for x in range(1000) for y in range (1000) })
#	mw.board.update_position ((997,997))

