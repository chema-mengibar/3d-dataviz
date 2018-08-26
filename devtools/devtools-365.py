import os
import random
from os import listdir
from os.path import isfile, join

import sys
import json

dataSet = []

numItems = 365
minValue = 0.01
maxValue = 0.2
decimals = 2

for d in range( 0, numItems ):
    dayCaptures = random.randint(0, 24)
    dayMeasures = []
    for dc in range( 0, dayCaptures ):
        measure = round( random.uniform( minValue, maxValue ), decimals )
        dayMeasures.append( measure )
    day = {
        "d": d,
        "v": dayMeasures
    }
    #v = random.randint(0, 5000)
    dataSet.append( day )

print dataSet

objData = {
  "data": dataSet
}

with open('./box/dataset_365_measures_2.json', 'w') as outfile:
    json.dump(objData, outfile)
