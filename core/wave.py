# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 18:08:38 2016

@author: Jan
"""
import yaml
class wave:
	def __init__(self, attacker, spawn_point):
		self.attacker = attacker #dict of the attacker (name:amount)
		self.spawn_point = spawn_point