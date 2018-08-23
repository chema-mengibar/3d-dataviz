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
with open( currentDir + "/datasets/dataset_simplelist_500.json") as f:
    jsonFile = json.load(f)
    data = jsonFile["data"]

#
# colors = ['uno','dos','tres']
#
# for d in data:
#
#     if d[3] >= 0 and d[3] <= 500:
#         color = colors[1]
#     elif d[3] > 500 and d[3] <= 1500:
#         color = colors[2]
#     else:
#         color = colors[0]


nCellsRow = 5 #25
nCellsCol = int( len( data ) / nCellsRow )

cursor = 0
for cX in range( 0, nCellsRow ):
    for cY in range( 0, nCellsCol ):
        dataCursor = data[ cursor ]
        cursor+=1

        aConfig = {
            'type':'plane',
            'mesh':'grid',
            'diameter':0.5,
            'h': dataCursor,
            'position':{
                'x': float( cX ),
                'y': float( cY ),
                'z': 0.0
            },
            'material': 'object_gradation_01'
        }

        creator = Creator( aConfig )
