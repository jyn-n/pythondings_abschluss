# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:52:00 2016

@author: Jan
"""
from data import attacker
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
		self.attacker_type = {"Goblin":yaml.load(open("data/attacker/goblin.yaml", "r"))}
		self.attacker = {}
		self.current_attacker_id = 0
		self.time = 0
		
		
	def spawn_wave(self, wave):
		sp = wave.spawn_point
		if sp not in self.field.spawn_points:
			sp = 0
		pos = self.field.spawn_points[sp]
		for name in wave.attacker:
			enemy = self.attacker_type[name]
			for x in range(wave.attacker[name]):
				self.attacker[self.current_attacker_id] = attacker(enemy, pos)
				self.current_attacker_id += 1
				
print(attacker)