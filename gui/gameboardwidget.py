from PyQt4 import QtGui, QtCore
Qt = QtCore.Qt

import itertools

class GameBoardWidget (QtGui.QFrame):

	def __init__ ( self, parent = None ):
		super().__init__(parent)

	def update_board ( board ):
		self._board = board

	def tile_size ( self ):
		return ( int(self.width() / self.board_dimension()[0]) , int(self.height()) / self.board_dimension()[1] )

	def tile_position ( self, position ):
		return list(map ( lambda x,y: x * y, self.tile_size(), position ))

	def board_dimension ( self ):
		return ( int(self.width() / 10), int(self.height() / 10) ) #TODO

	def paint_board ( self, board, position ):
		painter = QtGui.QPainter ( self )
		for p in itertools.product ( *map (range, self.board_dimension())):
			self.paint_tile ( painter, board[p], p ) #TODO
		painter.end()

	def paint_tile ( self, painter, tile, position):
		painter.fillRect ( *self.tile_position ( position ) , *self.tile_size() , self.get_color ( tile ) )
 
	@staticmethod
	def get_color ( tile ):
		return Qt.blue #TODO

	def paintEvent ( self, event ):
		super().paintEvent(event)
		print ("foo")
		board = dict()
		for p in itertools.product (range(1000), range(1000)): board[p] = 0 #TODO
		self.paint_board (board, (0,0))

