from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

import core.data.events as events
import core.data.constants as constants

import itertools
import math

class GameBoardWidget (QtGui.QWidget):

	click = QtCore.pyqtSignal(QtCore.QPoint)

	def __init__ ( self, parent = None ):
		super().__init__(parent)
		self._gamestate = None
		self._position = (0,0)

	def update_gamestate ( self, state ):
		self._gamestate = state

	def update_position ( self, position ):
		self._position = position

	def tile_size_pixels ( self ):
		return ( math.floor(self.width() / self.board_dimension()[0]) , math.floor(self.height() / self.board_dimension()[1]) )

	def tile_position_pixels ( self, position ):
		return tuple( x * y for (x,y) in zip (self.tile_size_pixels(), position) )

	def tile_position ( self, position ):
		r = tuple ( x + dx for (x,dx) in zip ( map ( lambda x,sx: math.floor ( x / sx ), position, self.tile_size_pixels() ) , self._position ) )
		for (x,max_x) in zip (r, self._gamestate.field.size()):
			if x >= max_x: return None
		return r

	def board_dimension ( self ):
		return ( self._gamestate.field.size() )

	def paint_board ( self, painter ):
		for p in itertools.product ( *( range(min(x,z), min(x+y, z)) for (x,y,z) in zip (self._position, self.board_dimension(), self._gamestate.field.size()) ) ):
			self.paint_tile ( painter, self._gamestate.field[p], tuple( (dv - v) for (dv, v) in zip ( p , self._position ) ) )

	def tile_rect ( self, position ):
		return QtCore.QRect ( *( self.tile_position_pixels (position) + self.tile_size_pixels())  )
		#this + stuff is unnessecary as of python 3.5.2 (or maybe earlier), just use * instead

	def tile_image ( self, tile ):
		return self._images['tiles'][tile.name()]

	def tile_overlay_image ( self, tile ):
		if tile.has_tower():
			return self._images['towers'][tile.get_tower().tower_type.name]

		if tile.is_spawn_point():
			return self._images['tiles']['Spawnpoint']

		if tile.is_target():
			return self._images['tiles']['Target']

		return None

	def paint_tile ( self, painter, tile, position ):
		painter.drawImage ( self.tile_rect (position) , self.tile_image (tile) )
		overlay = self.tile_overlay_image ( tile )
		if overlay != None:
			painter.drawImage ( self.tile_rect (position) , self.tile_overlay_image (tile) )

	def attacker_postition_pixels ( self, exact_position ):
		return tuple(x * sx / constants.distance + sx / 2 for (x,sx) in zip ( exact_position, self.tile_size_pixels() ) )

	def attacker_rect ( self, attacker, position_pixels ):
		ratio = 4
		return QtCore.QRect (*(tuple(v - dv // ratio for (v,dv) in zip ( position_pixels , self.tile_size_pixels() )) + tuple((v // ratio) * 2 for v in self.tile_size_pixels())))

	def paint_attacker ( self, painter, attacker ):
		position = self.attacker_postition_pixels ( self._gamestate.exact_position ( attacker ) )
		painter.drawImage ( self.attacker_rect (attacker, position) , self._images['attacker'][self._gamestate.attacker[attacker].name] )

	def paint_attackers ( self, painter ):
		for attacker in self._gamestate.attacker:
			self.paint_attacker ( painter, attacker )

	def paintEvent ( self, event ):
		super().paintEvent(event)
		painter = QtGui.QPainter ( self )
		self.paint_board (painter)
		self.paint_attackers (painter)
		painter.end()

	@staticmethod
	def event_pos_pixels ( event ):
		return (event.pos().x(), event.pos().y())

	def event_pos ( self, event ):
		return self.tile_position ( self.event_pos_pixels ( event ) )

	def mouseReleaseEvent ( self, event ):
		if (event.button() != QtCore.Qt.LeftButton): return
		if self.event_pos (event) == None: return

		self.click.emit (QtCore.QPoint(*self.event_pos (event) ))
		event.accept()

