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
	
	def load_level(self, level):
		lvl = yaml.load(open(level, "r"))
		self.field = yaml.load(open(lvl.field, "r"))
		self.towers = []
		for x in lvl.towers:
			self.towers.append(yaml.load(open(x, "r")))
		self.field = yaml.load(open(lvl.field, "r"))
		
		
		
x = game()
x.load_level("data/levels/1.yaml")