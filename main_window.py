from PyQt4 import QtCore, QtGui, uic
Qt = QtCore.Qt
import functools

import core.data.events as events

import shlex
import re
from pathlib import Path

ui_main_window, window_base_class = uic.loadUiType("main_window.ui") #TODO make path relative to own directory

image_path = 'images'
level_directory = 'data/levels'

class main_window ( window_base_class, ui_main_window ):

	event_answer = QtCore.pyqtSignal(str)

	def __init__ (self, parent = None, event_callback = None, gamestate = None, interval = 20):
		window_base_class.__init__(self, parent)
		ui_main_window.__init__(self)
		self.setupUi(self)

		self.input.ignore_keys ( Qt.Key_QuoteLeft )
		self.input.add_completion_items ( tuple (getattr(events, e) for e in dir(events) if not e.startswith('__')) )


		self.level_load.setFocus()
		self.level_load.add_completion_items ( tuple ( f.stem for f in Path(level_directory) if f.is_file() ) )

		self.load_images ( Path ( image_path ) )

		self.set_event_callback (event_callback)
		if gamestate != None:
			self.init_gamestate(gamestate)

		self.console.setVisible(False)

		self._timer = QtCore.QTimer()
		self._timer.timeout.connect ( functools.partial (self._event, events.tick) )
		self._timer.setInterval(interval)

	def toggle_pause (self):
		if self._timer.isActive():
			self._timer.stop()
		else:
			self._timer.start()

	def set_event_callback (self, callback):
		self._event = callback

	def load_level (self, name):
		self._event(events.load_level, name)

	def init_list_towers ( self , tower_types):
		self.list_towers.clear()
		for tower in tower_types:
			self.list_towers.addItem (tower)
		self.list_towers.setCurrentRow(0)

	def init_wave_view ( self , waves ):
		self.waves.clear()

		self.waves.setColumnCount (4)
		self.waves.setRowCount (functools.reduce ( (lambda x,y: len(waves[x].attacker) + len(waves[y].attacker)), waves ) )

		i = 0
		for wave in waves:
			self.waves.setItem ( i, 0, QtGui.QTableWidgetItem ( str(wave) ) )
			self.waves.setItem ( i, 1, QtGui.QTableWidgetItem ( str(waves[wave].spawn_point) ) )
			for attacker in waves[wave].attacker:
				self.waves.setItem ( i, 2, QtGui.QTableWidgetItem ( attacker ) )
				self.waves.setItem ( i, 3, QtGui.QTableWidgetItem ( str ( waves[wave].attacker [attacker] ) ) )
				i += 1

	def init_gamestate (self, gamestate):
		self.board.update_gamestate(gamestate)
		self.update_gamestate ( gamestate )

		self.init_list_towers (gamestate.tower_type)
		self.init_wave_view (gamestate.waves)

		self._timer.start()

	def draw_gamestate ( self , gamestate ):
		self.money.setText ( str (gamestate.money) )
		self.life.setText ( str (gamestate.life) )
		self.time.setText ( str (gamestate.time) )

	def update_gamestate (self, gamestate):
		self._gamestate = gamestate
		self.draw_gamestate ( gamestate )
		self.board.update_gamestate(gamestate)
		self.repaint()

	def game_board_clicked (self, position):
		position = (position.x(), position.y()) #TODO pass a tuple to slot
		if self._gamestate.field [position].has_tower ():
			self.show_tower_type ( self._gamestate.field [position].get_tower().tower_type )
		else:
			self._event ( events.place_tower , str ( self.list_towers.currentItem().text() ) , position ) 

	def submit_console (self, text):
		self.submit_console_split ( *shlex.split(text) )

	@staticmethod
	def parse_arg ( arg ):
		try:
			i = int(arg)
			return i
		except ValueError:
			pass
		except TypeError:
			pass

		if arg[0] == '(' and arg[-1] == ')':
			return tuple(main_window.parse_args ( *arg[1:len(arg)-1].split(',')  ))

		return arg

	@staticmethod
	def parse_args ( *args ):
		return map (main_window.parse_arg, args)

	def submit_console_split (self, event_name, *args):
		self.event_answer.emit ( str ( self._event ( event_name, *self.parse_args(*args) ) ) )

	def toggle_console_visibility ( self ):
		self.console.setVisible ( not self.console.isVisible() )
		if self.console.isVisible():
			self.input.setFocus()

	def keyPressEvent ( self, event ):
		if event.key() == Qt.Key_QuoteLeft:
			self.toggle_console_visibility()
			event.accept()
			return

		super().keyPressEvent (event)

	def show_tower_type_by_item ( self, tower_item ):
		return self.show_tower_type ( self._gamestate.tower_type[tower_item.text()] )

	def show_tower_type ( self, tower_type ):
		self.tower_type_info.show_tower_type ( tower_type )

	def show_attacker_type_by_item ( self, attacker_item ):
		return self.show_attacker_type ( self._gamestate.attacker_type[attacker_item.text()] )

	def show_attacker_type_by_row ( self, row ):
		return self.show_attacker_type_by_item ( self.waves.item (row, 2) )

	def show_attacker_type ( self, attacker_type ):
		self.attacker_type_info.show_attacker_type ( attacker_type )

	def load_images ( self , image_directory ):
		self.board._images = main_window.load_directory (image_directory)

	@staticmethod
	def load_directory ( directory ):
		r = dict ()
		for f in directory.glob('*'):
			r[f.stem] = main_window.load_file (f)
		return r

	@staticmethod
	def load_file ( f ):
		if f.is_dir():
			return main_window.load_directory (f)
		if f.is_file():
			return QtGui.QImage (f.as_posix())
