from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

class ConsoleEdit (QtGui.QLineEdit):

	submit = QtCore.pyqtSignal(str)

	def __init__ ( self, parent = None ):
		super().__init__(parent)
		self.completion_items = tuple()

	def add_completion_items ( self, items ):
		self.completion_items += items

	def keyPressEvent ( self, event ):
		if event.key() == Qt.Key_Return:
			self.submit.emit(self.text())
			event.accept()
			return

		if event.key() != Qt.Key_Tab:
			super().keyPressEvent(event)
			return

		for item in self.completion_items:
			if item.startswith(self.text()):
				self.setText(item)
				event.accept()
				break

