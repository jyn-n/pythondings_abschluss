
from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

class ConsoleView (QtGui.QListWidget):
	def __init__ ( self, parent = None ):
		super().__init__(parent)

	def submit (self, text):
		self.addItem ( '>> ' + text )
		self.setCurrentRow ( -1 )
