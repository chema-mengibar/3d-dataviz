import os
from os import listdir
from os.path import isfile, join
from math import cos, sin, pi

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
with open( currentDir + "/datasets/data_dots-100.json") as f:
    jsonFile = json.load(f)
    data = jsonFile["data"]

for d in data:
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
        'material': 'base'
    }

    creator = Creator( aConfig )
