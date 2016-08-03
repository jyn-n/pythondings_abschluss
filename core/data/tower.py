# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:05:55 2016

@author: Jan
"""

class tower:
	def __init__(self, tower_type):
		self.tower_type = tower_type
		self._cooldown = 0
		
	def tick(self):
		if self._cooldown > 0:
			self._cooldown -= 1
			
	def fire(self):
		self._cooldown = self.tower_type.attack_time
		
	def can_fire(self):
		return self._cooldown == 0