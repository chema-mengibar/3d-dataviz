import os
from os import listdir
from os.path import isfile, join

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
with open( currentDir + "/datasets/blender-001-dots-dataset01.json") as f:
    jsonFile = json.load(f)
    data = jsonFile["data"]

print( data )

colors = ['uno','dos','tres']

for d in data:

    if d[3] >= 0 and d[3] <= 500:
        color = colors[1]
    elif d[3] > 500 and d[3] <= 1500:
        color = colors[2]
    else:
        color = colors[0]

    aConfig = {
        'type':'sphere',
        'mesh':'Basic_Sphere',
        'u':20,
        'v':10,
        'diameter':0.1,
        #'modifier':'SUBSURF',
        'position':{
            'x': d[0],
            'y': d[1],
            'z': d[2]
        },
        'material': color
    }

    creator = Creator( aConfig )
