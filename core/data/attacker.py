# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 16:25:11 2016

@author: Jan
"""
#from .attacker_type import attacker_type
class attacker:
	def __init__(self, attacker_type, position):
		self.attacker_type = attacker_type
		self._hp = self.attacker_type.hp
		self.name = self.attacker_type.name
		self.position = position
		self.progress = 0
		
	def get_hp(self):
		return self._hp
		
	def take_damage(self, dmg):
		self._hp -= dmg
		return self._hp >= 0