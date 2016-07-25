# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:27:54 2016

@author: Jan
"""

from core import game
gg = game()
gg.load_level("data/levels/1.yaml")
gg.spawn_wave(gg.waves[1])
gg.attacker[0].take_damage(5)
for x in gg.attacker:
	print(x, gg.attacker[x].position)
gg.move_attackers()
for x in gg.attacker:
	print(x, gg.attacker[x].position)