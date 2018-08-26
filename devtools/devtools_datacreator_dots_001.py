import os
import random
from os import listdir
from os.path import isfile, join

import sys
import json

dataSet = []


for x in range(0, 100):
  x = random.uniform(1, 20)
  y = random.uniform(1, 20)
  z = random.uniform(1, 20)
  v = random.randint(0, 5000)
  row = [ round(x,2) , round(y,2), round(z,2), v]
  dataSet.append( row )

objData = {
  "data": dataSet
}

with open('./box/data_dots-100.json', 'w') as outfile:
    json.dump(objData, outfile)
