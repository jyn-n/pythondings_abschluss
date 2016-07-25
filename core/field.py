# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:21:45 2016

@author: Jan
"""


class tile:
	def __init__(self):
		self._accessable = True
		self._buildable = True
		self._tower = None
		
	def add_tower(self, tower):
		if self._tower == None:
			self._tower = tower
		else:
			raise Exception("tower already present") 

	def has_tower(self):
		return not(self._tower == None)
		
	def delete_tower(self):
		self._tower = None
		
	def get_tower(self):
		return self._tower
		
	def is_accessable(self):
		return self._accessable and not self.has_tower()
		
	def is_buildable(self):
		return self._buildable and not self.has_tower()
		
	def make_accessable(self):
		self._accessable = True
		
	def make_buildable(self):
		self._buildable = True
		
	def make_unaccessable(self):
		self._accessable = False
		
	def make_unbuildable(self):
		self._buildsable = False
		

class field:
	def __init__(self, n, m):
		self._size = (n,m)
		self._tiles = { (i,j) : tile() for i in range(n) for j in range(m) }

	def __getitem__(self, v):
		return self._tiles[v]

	def size (self):
		return self._size

	def __iter__(self):
		return self._tiles.__iter__()

	def get_towers(self):
		return { t : self[t].get_tower() for t in self if self[t].has_tower() }

