# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:01:01 2016

@author: Jan
"""

from core import *
import yaml


x = field(20,20, {0:(0,0)}, [(19,19)])
x[0,1].make_unaccessible()
x[2,2].make_unaccessible()
yaml.dump(x, open("data/fields/field1.yaml", "w"))


y = tower_type("Laser Tower", 5000, 1, 2, 7)
yaml.dump(y, open("data/towers/laser_tower.yaml", "w"))
z = tower_type("Small Tower", 2, 2, 2, 2)
yaml.dump(z, open("data/towers/small_tower.yaml", "w"))

a = attacker_type("Goblin", 10, 100, 100)
yaml.dump(a, open("data/attacker/goblin.yaml", "w"))
b = attacker_type("Orc", 2, 5, 5)
yaml.dump(b, open("data/attacker/orc.yaml", "w"))

c = level(["data/towers/laser_tower.yaml"], "data/fields/field1.yaml",
	{1 : wave({"Goblin":5}, 0), 2 : wave({"Goblin":3, "Orc": 5}, 0)}, 1, 10)
yaml.dump(c, open("data/levels/1.yaml", "w"))