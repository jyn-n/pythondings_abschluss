# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:01:01 2016

@author: Jan
"""

import core
import yaml
x = field(5,3)
x.make_unaccessable(2,2)
b = tower("","","","","")
x.add_tower(b, 3,1)
a = open("field1.yaml", "w")
yaml.dump(x, a)