import os
import random
from os import listdir
from os.path import isfile, join

import sys
import json

dataSet = []

numItems = 500
minValue = 0
maxValue = 10
decimals = 2

for x in range( 0, numItems ):
  y = round( random.uniform( minValue, maxValue ), decimals )
  #v = random.randint(0, 5000)
  row = y
  dataSet.append( row )

objData = {
  "data": dataSet
}

with open('./box/dataset_simplelist_500.json', 'w') as outfile:
    json.dump(objData, outfile)
