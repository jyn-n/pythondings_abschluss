# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:52:00 2016

@author: Jan
"""
import core
import yaml
class game:
	def __init__(self):
		pass
	
	def load_level(self, level): #level is the path of the level file
		lvl = yaml.load(open(level, "r"))
		self.field = yaml.load(open(lvl.field, "r"))
		self.towers = []
		for x in lvl.towers:
			self.towers.append(yaml.load(open(x, "r")))
		self.waves = lvl.waves
		
		
		#TODO: load all attackers types (dict name:object)
		self.attacker_type = None
		self.attacker = {}
		
		self.time = 0
		
	def spawn_wave(self, wave):
		pass