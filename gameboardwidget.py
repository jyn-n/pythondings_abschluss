from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

import core.data.events as events
import core.data.constants as constants

import itertools
import math

class GameBoardWidget (QtGui.QFrame):

	click = QtCore.pyqtSignal(QtCore.QPoint)

	def __init__ ( self, parent = None ):
		super().__init__(parent)
		self._gamestate = None
		self._position = (0,0)

	def update_gamestate ( self, state ):
		self._gamestate = state

	def update_position ( self, position ):
		self._position = position

	def tile_size ( self ):
		return ( math.floor(self.width() / self.board_dimension()[0]) , math.floor(self.height() / self.board_dimension()[1]) )

	def tile_position ( self, position ):
		return ( x * y for (x,y) in zip (self.tile_size(), position) )

	def tile_coords ( self, position ):
		r = tuple ( x + dx for (x,dx) in zip ( map ( lambda x,sx: math.floor ( x / sx ), position, self.tile_size() ) , self._position ) )
		for (x,max_x) in zip (r, self._gamestate.field.size()):
			if x >= max_x: return None
		return r

	def board_dimension ( self ):
		return ( math.floor(self.width() / 30), math.floor(self.height() / 30) ) #TODO

	def paint_board ( self, painter ):
		for p in itertools.product ( *( range(min(x,z), min(x+y, z)) for (x,y,z) in zip (self._position, self.board_dimension(), self._gamestate.field.size()) ) ):
			self.paint_tile ( painter, self._gamestate.field[p], ( (dv - v) for (dv, v) in zip ( p , self._position ) ) )

	def paint_tile ( self, painter, tile, position):
		painter.fillRect ( * ( tuple(self.tile_position ( position )) + tuple(self.tile_size()) + (self.tile_brush ( tile ),) ) ) #this tuple + stuff is unnessecary as of python 3.5.2 (or maybe earlier), just use * instead
 
	@staticmethod
	def tile_brush ( tile ):
		if ( tile.has_tower() ): return Qt.black
		return { (True,True):Qt.blue, (True,False):Qt.green, (False,True):Qt.red, (False,False):Qt.yellow } [ tile.is_accessible(), tile.is_buildable() ] #TODO

	def attacker_position ( self, exact_position ):
		return map ( lambda x,sx: x * sx / constants.distance for (x,sx) in zip ( exact_position, self.tile_size() ) )

	def paint_attacker ( self, painter, attacker ):
		position = attacker_position ( self._gamestate.exact_position ( attacker ) )
		painter.setColor (QtCore.Qt.pink)
		painter.drawEllipse(QtCore.QPointF ( *position , 5, 5 ) ) #TODO

	def paint_attackers ( self, painter ):
		for attacker in self._gamestate.attacker:
			self.paint_attacker ( painter, attacker )

	def paintEvent ( self, event ):
		super().paintEvent(event)
		painter = QtGui.QPainter ( self )
		self.paint_board (painter)
		self.paint_attackers (painter)
		painter.end()

	def mouseReleaseEvent ( self, event ):
		if (event.button() != QtCore.Qt.LeftButton): return
		self.click.emit (QtCore.QPoint(*self.tile_coords ( (event.pos().x(), event.pos().y()) ) ))

