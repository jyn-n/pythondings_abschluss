# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:52:00 2016

@author: Jan
"""
from .data import *
import yaml
import math
import random
class game:
	def __init__(self, event):
		self.event = event
		pass
	
	def load_level(self, level): #level is the path of the level file
		lvl = yaml.load(open(level, "r"))
		self.field = yaml.load(open(lvl.field, "r"))
		self.towers = {}
		for x in lvl.towers:
			twr = yaml.load(open(x, "r"))
			self.towers[twr.name] = twr
		self.waves = lvl.waves
		
		
		#TODO: load all attackers types (dict name:object)
		self.attacker_type = {"Goblin":yaml.load(open("data/attacker/goblin.yaml", "r"))}
		self.attacker = {}
		self.current_attacker_id = 0
		self.time = 0
		
	def place_tower(self, tower, pos):
		self.field[pos[0], pos[1]].add_tower(self.towers[tower])
		
	def spawn_wave(self, wave):
		sp = wave.spawn_point
		if sp not in self.field.spawn_points:
			sp = 0
		pos = self.field.spawn_points[sp]
		for name in wave.attacker:
			for x in range(wave.attacker[name]):
				self.event(events.spawn_attacker, name, pos)
				
				
	def spawn_attacker(self, name, pos):
		enemy = self.attacker_type[name]
		self.attacker[self.current_attacker_id] = attacker(enemy, pos)
		self.current_attacker_id += 1
				
	
	def move(self, i):
		self.attacker[i].progress += self.attacker[i].attacker_type.speed
		pos = self.exact_position(i)
		self.attacker[i].position = (pos[0] // constants.distance, pos[1] // constants.distance)
		self.attacker[i].progress = self.attacker[i].progress % constants.distance

	def move_all(self):
		for i in self.attacker:
			self.event(events.move, i)
			
	def exact_position(self, i):
		x = self.attacker[i].position[0]
		y = self.attacker[i].position[1]
		dx = self.field[x, y].next_tile[0] * self.attacker[i].progress
		dy = self.field[x, y].next_tile[1] * self.attacker[i].progress
		return (constants.distance * x + dx, constants.distance * y + dy)
		
	def attackers_in_range(self, pos1):
		attir = []
		for att in self.attacker:
			pos2 = self.exact_position(att)
			x = math.sqrt((pos1[0] * constants.distance - pos2[0])**2 + (pos1[1] * constants.distance - pos2[1])**2)
			if x < self.field[pos1[0], pos1[1]].get_tower().attack_range:
				attir.append(att)
		return attir

		
	def die(self, i):
		del self.attacker[i]
		
	def take_damage(self, i, amount):
		if self.attacker[i].take_damage:
			self.event(events.die, i)
			
	def fire_tower(self, pos):
		if self.field[pos[0], pos[1]].has_tower:
			twr = self.field[pos[0], pos[1]].get_tower
			attir = self.attackers_in_range(pos)
			for i in range(twr.fire_rate):
				rand = random.randrange(len(attir))
				self.event(events.take_damage, attir[i], twr.game)

