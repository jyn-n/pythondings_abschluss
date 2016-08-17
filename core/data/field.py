# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:21:45 2016

@author: Jan
"""
from .tower import tower
class tile:
	def __init__(self, pos, sp, target):
		self._accessible = True
		self._buildable = True
		self._tower = None
		self.next_tile = (1,0)
		self.position = pos
		self._spawn_point = sp
		self._target = target
		
	def add_tower(self, twr):
		if self._tower == None:
			self._tower = tower(twr)
		else:
			raise Exception("tower already present") 

	def has_tower(self):
		return not(self._tower == None)
		
	def delete_tower(self):
		self._tower = None
		
	def get_tower(self):
		return self._tower
		
	def get_tower_type(self):
		return self._tower.tower_type
		
	def is_accessible(self):
		return self._accessible and not self.has_tower()
		
	def is_buildable(self):
		return self._buildable and not self.has_tower()
	
	def is_target(self):
		return self._target
		
	def is_spawn_point(self):
		return self._spawn_point
		
	def make_accessible(self):
		self._accessible = True
		
	def make_buildable(self):
		self._buildable = True
		
	def make_unaccessible(self):
		self._accessible = False
		
	def make_unbuildable(self):
		self._buildable = False

	def name ( self ):
		return str(self.is_accessible()) + str (self.is_buildable())

class field:
	def __init__(self, n, m, spawn_points, targets):
		self._size = (n,m)
		self._tiles = { (i,j) : tile((i,j), (i,j) in spawn_points.values(), (i,j) in targets) for i in range(n) for j in range(m) }
		self.spawn_points = spawn_points #dict of spawn ponits (id: position)
		self.targets = targets #list of positions

	def __getitem__(self, v):
		return self._tiles[v]

	def size (self):
		return self._size

	def __iter__(self):
		return self._tiles.__iter__()

	def get_towers(self):
		return { t : self[t].get_tower() for t in self if self[t].has_tower() }

