# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:27:54 2016

@author: Jan
"""

from core import game
print(game)
gg = game()
gg.load_level("data/levels/1.yaml")
gg.spawn_wave(gg.waves[1])