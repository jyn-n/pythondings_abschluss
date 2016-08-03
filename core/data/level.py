# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:06:22 2016

@author: Jan
"""

class level:
	def __init__(self, tower_type, field, waves, life, money):
		self.tower_type = tower_type #list of towers filenames
		self.field = field
		self.waves = waves #dict of waves (time:wave)
		self.life = life
		self.starting_money = money
		
		
	