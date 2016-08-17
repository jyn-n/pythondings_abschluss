from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

class Infowidget (QtGui.QTableWidget):
	def __init__ ( self, parent = None ):
		super().__init__(parent)

	@staticmethod
	def tower_type_data (tower_type):
		return (
			  ('Name' , tower_type.name)
			, ('Range' , tower_type.attack_range)
			, ('Cooldown' , tower_type.attack_time)
			, ('Cost' , tower_type.money)
			, ('Damage' , tower_type.damage)
			)

	@staticmethod
	def attacker_type_data (attacker_type):
		return (
			  ('Name' , attacker_type.name)
			, ('Speed' , attacker_type.speed)
			, ('Maximum Life' , attacker_type.hp)
			, ('Value' , attacker_type.money)
			)

	def show_tower_type ( self, tower_type ):
		return self.show_data ( self.tower_type_data (tower_type) )

	def show_attacker_type ( self, attacker_type ):
		return self.show_data ( self.attacker_type_data (attacker_type) )

	def show_data ( self, items ):
		self.clear()

		self.setRowCount(len(items))
		self.setColumnCount(2)

		for (i, (name, value)) in enumerate(items):
			self.setItem (i, 0, QtGui.QTableWidgetItem ( name ) )
			self.setItem (i, 1, QtGui.QTableWidgetItem ( str(value) ) )
