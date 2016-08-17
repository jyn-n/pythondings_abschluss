# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:01:01 2016

@author: Jan
"""

from core import *
import yaml


x = field(35,21, {0:(0,4), 1: (0,17)}, [(34,10)])

for i in range(5,16):
	x[6,i].make_unaccessible()
		
for i in range(4,17):
	for j in range(6,8):
		x[j,i].make_unbuildable()
	
for i in range(8, 13):
	for j in range(10, 20):
		x[j,i].make_unaccessible()
		
for i in range(7):
	x[28,i].make_unaccessible()
	x[28,i].make_unbuildable()
	
for i in range(14, 21):
	x[28,i].make_unaccessible()
	x[28,i].make_unbuildable()
	
for i in range(11, 28):
	for j in range(4):
		x[i,j].make_unaccessible()
	for j in range(17, 21):
		x[i,j].make_unaccessible()
yaml.dump(x, open("data/fields/Field1.yaml", "w"))



y = tower_type("Laser Tower", 5000, 1, 2, 7)
yaml.dump(y, open("data/towers/Laser Tower.yaml", "w"))
z = tower_type("Small Tower", 2, 2, 2, 2)
yaml.dump(z, open("data/towers/Small Tower.yaml", "w"))

a = attacker_type("Goblin", 10, 100, 100)
yaml.dump(a, open("data/attacker/Goblin.yaml", "w"))
b = attacker_type("Orc", 2, 5, 5)
yaml.dump(b, open("data/attacker/Orc.yaml", "w"))

c = level(["Laser Tower"], "Field1",
	{1 : wave({"Goblin":5}, 0), 2 : wave({"Goblin":3, "Orc": 5}, 0)}, 1, 10)
yaml.dump(c, open("data/levels/1.yaml", "w"))
