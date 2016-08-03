
from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

class ConsoleView (QtGui.QTextBrowser):
	def __init__ ( self, parent = None ):
		super().__init__(parent)

	def submit (self, text):
		self.append ( '>> ' + text )
