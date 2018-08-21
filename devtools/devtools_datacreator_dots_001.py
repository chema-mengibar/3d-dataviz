import os
import random
from os import listdir
from os.path import isfile, join

import sys
import json

dataSet = []


for x in range(0, 1500):
  x = random.uniform(1, 10)
  y = random.uniform(1, 10)
  z = random.uniform(1, 10)
  v = random.randint(0, 5000)
  row = [ round(x,2) , round(y,2), round(z,2), v]
  dataSet.append( row )

objData = {
  "data": dataSet
}

with open('../data/data_dots-001.json', 'w') as outfile:
    json.dump(objData, outfile)
