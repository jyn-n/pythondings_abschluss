from PyQt4 import QtCore, QtGui, uic
import sys
import itertools

ui_main_window, window_base_class = uic.loadUiType("main_window.ui")


class main_window ( window_base_class, ui_main_window ):
	def __init__ (self, parent = None):
		window_base_class.__init__(self, parent)
		ui_main_window.__init__(self)
		self.setupUi(self)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	mw = main_window()
	mw.show()
	sys.exit(app.exec_())

