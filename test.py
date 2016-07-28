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
gg.place_tower("Laser Tower", (6,0))
print(gg.attackers_in_range((6,0)))
gg.move_attackers()
print(gg.attacker[0].position)
print(gg.attackers_in_range((6,0)))
gg.move_attackers()
print(gg.attacker[0].position)
print(gg.attackers_in_range((6,0)))
gg.move_attackers()
print(gg.attacker[0].position)
print(gg.attackers_in_range((6,0)))
gg.move_attackers()
print(gg.attacker[0].position)
print(gg.attackers_in_range((6,0)))
	
print(gg.exact_position(0))