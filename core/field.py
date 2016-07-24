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
		self._tiles = {}
		for i in range(n):
			for j in range(m):
				self._tiles[i, j] = tile()
				
	def is_accessable(self, x, y):
		return self._tiles[x, y].is_accessable()
		
	def is_buildable(self, x, y):
		return self._tiles[x, y].is_buildable()
		
	def make_accessable(self, x, y):
		self._tiles[x, y].make_accessable()
		
	def make_buildable(self, x, y):
		self._tiles[x, y].make_buildable()
		
	def make_unaccessable(self, x, y):
		self._tiles[x, y].make_unaccessable()
		
	def make_unbuildable(self, x, y):
		self._tiles[x, y].make_unbuildable()
		
	def add_tower(self, tower, x, y):
		self._tiles[x, y].add_tower(tower)
		
	def delete_tower(self, x, y):
		self._tiles[x, y].delete_tower()
		
	def has_tower(self, x, y):
		return self._tiles[x, y].has_tower()
	
	def get_tower(self, x, y):
		return self._tiles[x,y].get_tower()
		
	def get_towers(self):
		x = {}
		for a in _tiles:
			if has_tower(a[0],a[1]):
				x[a] = get_tower(a[0],a[1])
			
		

		
"""
x = open("field.yaml", "r")
b = yaml.load(x)
b.foo()"""



