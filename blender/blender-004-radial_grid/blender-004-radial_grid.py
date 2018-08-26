import os
from os import listdir
from os.path import isfile, join
from math import cos, sin, pi

import sys
import json

currentDir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
currentFileName = os.path.basename(__file__)

libDir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../"))
print(libDir)

sys.path.append( libDir )

from script.lib.creator import *
import script
import importlib
importlib.reload( script.lib.creator )
from script.lib.creator import Creator

#--------------------------------------------------------------
with open( currentDir + "/datasets/dataset_365_measures_2.json") as f:
    jsonFile = json.load(f)
    data = jsonFile["data"]

colors = ['uno','dos','tres']

for da in data:
    angle = da["d"] * pi/180 #radians
    center = [0,0]

    for i, v in enumerate( da["v"] ):

        if v >= 0 and v <= 0.1:
            color = colors[1]
        elif v > 0.1 and v <= 0.2:
            color = colors[2]
        else:
            color = colors[0]

        radius = i + 10 # margin from center
        _x = float( center[0] + (radius * cos(angle)) )
        _y = float( center[1] + (radius * sin(angle)) )

        aConfig = {
            'type':'sphere',
            'mesh':'dm',
            'u':20,
            'v':10,
            'diameter': v,
            #'modifier':'SUBSURF',
            'position':{
                'x': _x,
                'y': _y,
                'z': 2.0
            },
            'material': color
        }

        creator = Creator( aConfig )
