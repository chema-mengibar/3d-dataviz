import os
from os import listdir
from os.path import isfile, join
from math import cos, sin, pi
import random
import sys
import json

currentDir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
currentFileName = os.path.basename(__file__)

libDir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../"))
sys.path.append( libDir )

from script.lib.creator import *
from script.lib.selector import *

import script
import importlib

importlib.reload( script.lib.creator )
importlib.reload( script.lib.selector )

from script.lib.creator import Creator
from script.lib.selector import Selector
selector = Selector()

#--------------------------------------------------------------
#STEP: replace the prefix of the items to connect
selector.selectByName( 'Basic_Sphere' )
selectedObjectsLocation = selector.locationSelectedObjects()

with open( currentDir + "/datasets/data_network-items.json") as f:
    jsonFile = json.load(f)
    networkItems = jsonFile["data"]

colors = ['uno','dos','tres']

weightOptions = ["a","=","b"]

for ni in networkItems:
    _fromItem =  ni[ 'from' ]
    _toItem = ni[ 'to' ]
    _relation = ni[ 'relation' ]

    if _relation >= 0 and _relation <= 500:
        color = colors[1]
    elif _relation > 500 and _relation <= 4000:
        color = colors[2]
    else:
        color = colors[0]

    _weight = random.randint( 0, 2 )

    aConfig = {
        'type':'path',
        'mesh':'linea',
        'radius': 0.025,
        #'modifier':'SUBSURF',
        'pointA':{
            'x': selectedObjectsLocation[ _fromItem ]['location'][0],
            'y': selectedObjectsLocation[ _fromItem ]['location'][1],
            'z': selectedObjectsLocation[ _fromItem ]['location'][2]
        },
        'pointB':{
            'x': selectedObjectsLocation[ _toItem ]['location'][0],
            'y': selectedObjectsLocation[ _toItem ]['location'][1],
            'z': selectedObjectsLocation[ _toItem ]['location'][2]
        },
        'weight': weightOptions[ _weight ],
        'force':  (_relation / 5000),
        'material': color
    }

    creator = Creator( aConfig )
