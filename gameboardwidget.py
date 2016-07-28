from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

import core.data.events as events

import itertools
import math

class GameBoardWidget (QtGui.QFrame):

	def __init__ ( self, parent = None ):
		super().__init__(parent)
		self._gamestate = None
		self._position = (0,0)

	def set_event_callback ( self, callback ):
		self.event = callback

	def update_gamestate ( self, state ):
		self._gamestate = state

	def update_position ( self, position ):
		self._position = position

	def tile_size ( self ):
		return ( math.floor(self.width() / self.board_dimension()[0]) , math.floor(self.height() / self.board_dimension()[1]) )

	def tile_position ( self, position ):
		return ( x * y for (x,y) in zip (self.tile_size(), position) )

	def pos_to_tile_coords ( self, position ):
		return map ( lambda x,sx: math.floor ( x / sx ), position, self.tile_size() )

	def board_dimension ( self ):
		return ( math.floor(self.width() / 30), math.floor(self.height() / 30) ) #TODO

	def paint_board ( self ):
		painter = QtGui.QPainter ( self )
		for p in itertools.product ( *( range(min(x,z), min(x+y, z)) for (x,y,z) in zip (self._position, self.board_dimension(), self._gamestate.field.size()) ) ):
			self.paint_tile ( painter, self._gamestate.field[p], ( (dv - v) for (dv, v) in zip ( p , self._position ) ) )
		painter.end()

	def paint_tile ( self, painter, tile, position):
		painter.fillRect ( *(self.tile_position ( position ) + self.tile_size()) + (self.get_brush ( tile ),) ) #this + is unnessecary as of python 3.5.2 (or maybe earlier), just use a second * instead
 
	@staticmethod
	def get_brush ( tile ):
		if ( tile.has_tower() ): return Qt.black
		return { (True,True):Qt.blue, (True,False):Qt.green, (False,True):Qt.red, (False,False):Qt.yellow } [ tile.is_accessible(), tile.is_buildable() ] #TODO

	def paintEvent ( self, event ):
		super().paintEvent(event)
		self.paint_board ()

	def mousePressEvent ( self, event ):
		if (event.button() != QtCore.Qt.LeftButton): return
		#self.event ( events.place_tower

