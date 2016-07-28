# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:06:22 2016

@author: Jan
"""

class level:
	def __init__(self, towers, field, waves, life):
		self.towers = towers #list of towers filenames
		self.field = field
		self.waves = waves #dict of waves (time:wave)
		self.life = life
		
	