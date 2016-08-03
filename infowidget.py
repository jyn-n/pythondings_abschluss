from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

class Infowidget (QtGui.QTableWidget):
	def __init__ ( self, parent = None ):
		super().__init__(parent)

	@staticmethod
	def tower_type_type_data (tower_type):
		return  (
		  ('Name' , tower_type.name)
		, ('Range' , tower_type.attack_range)
		, ('Cooldown' , tower_type.attack_time)
		, ('Cost' , tower_type.money)
		, ('Damage' , tower_type.damage)
		)

	def show_tower_type ( self, tower_type ):
		items = self.tower_data(tower_type)
		self.clear()

		self.setRowCount(len(items))
		self.setColumnCount(2)

		for (i, (name, value)) in enumerate(items):
			self.setItem (i, 0, QtGui.QTableWidgetItem ( name ) )
			self.setItem (i, 1, QtGui.QTableWidgetItem ( str(value) ) )
