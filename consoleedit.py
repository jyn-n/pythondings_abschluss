from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

class ConsoleEdit (QtGui.QLineEdit):

	submit = QtCore.pyqtSignal(str)

	def __init__ ( self, parent = None ):
		super().__init__(parent)
		self._completion_items = tuple()
		self._history = tuple()
		self.reset()

	def reset ( self , text=True):
		if (text): self.setText('')
		self._completion = ''
		self._history_count = -1

	def commit ( self ):
		if self.text() != '':
			self.submit.emit(self.text())
			self._history = (self.text(),) + self._history
			self.reset()

	def add_completion_items ( self, items ):
		self._completion_items += items

	def autocomplete ( self ):
		c = False
		if self._completion == '':
			c = True
			self._completion = self.text()

		for item in self._completion_items:
			if item.startswith(self._completion) and c:
				self.setText(item)
				return
			if item == self.text():
				c = True

		for item in self._completion_items:
			if item.startswith(self._completion):
				self.setText(item)
				return

	def event ( self, event ):
		if (event.type()==QtCore.QEvent.KeyPress) and (event.key()==Qt.Key_Tab):
			self.autocomplete()
			event.accept()
			return True

		return super().event ( event )

	def next_history ( self ):
		if self._history_count < len(self._history)-1:
			self._history_count += 1
		if self._history_count >= 0:
			self.setText(self._history[self._history_count])

	def prev_history ( self ):
		if self._history_count > -1:
			self._history_count -= 1

		if self._history_count >= 0:
			self.setText(self._history[self._history_count])
		else:
			self.setText('')

	def keyPressEvent ( self, event ):
		actions = {
				Qt.Key_Return : self.commit ,
				Qt.Key_Up : self.next_history ,
				Qt.Key_Down : self.prev_history
			}

		if event.key() in actions:
			actions[event.key()]()
			event.accept()
			return

		self.reset(False)
		super().keyPressEvent(event)

