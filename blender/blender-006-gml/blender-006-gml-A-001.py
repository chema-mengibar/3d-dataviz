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
from script.lib.geo import *

import script
import importlib

importlib.reload( script.lib.creator )
importlib.reload( script.lib.selector )
importlib.reload( script.lib.geo )

from script.lib.creator import Creator
from script.lib.selector import Selector
from script.lib.geo import Geo
selector = Selector()
geo = Geo()

#--------------------------------------------------------------
with open( currentDir + "/datasets/dataset_coordenadas_0.json") as f:
    jsonFile = json.load(f)
    data = jsonFile["data"]

geo.setEarthRadius( 2 )

for d in data:

    _lon = d['lon']
    _lat = d['lat']

    xyz = geo.coorToXyz( _lat, _lon, 0 )
    print( xyz[0], xyz[1], xyz[2] )
    aConfig = {
        'type':'sphere',
        'mesh':'Basic_Sphere',
        'u':20,
        'v':10,
        'diameter':0.025,
        #'modifier':'SUBSURF',
        'position':{
            'x': xyz[0],
            'y': xyz[1],
            'z': xyz[2]
        },
        'material': 'tres'
    }
    creator = Creator( aConfig )
