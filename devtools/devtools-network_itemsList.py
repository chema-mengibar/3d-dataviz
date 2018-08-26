import os
import random
from os import listdir
from os.path import isfile, join

import sys
import json

dataSet = []

baseName = 'Plane'

numConnections = 200
minItemsU = 1
maxItemsU = 4

minItemsW = 5
maxItemsW = 8


addZeros = 3

dataSet = []
similars = 0;

for x in range(0, numConnections):

    suffixA =  '.' + str( random.randint( minItemsU, maxItemsU ) ).zfill( addZeros )
    if suffixA == '.000':
        suffixA = ''
    nameA =  baseName + suffixA

    suffixB =  '.' + str( random.randint( minItemsW, maxItemsW ) ).zfill( addZeros )
    if suffixB == '.000':
        suffixB = ''
    nameB =  baseName + suffixB

    _relation =  random.randint( 1, 5000 )

    if suffixA != suffixB:
        dataSet.append( { 'from': nameA, 'to': nameB, 'relation': _relation } )
    else:
        similars+=1

objData = {
  "data": dataSet
}

print 'similars ' + str( similars )
with open('./box/data_network-items_blocks.json', 'w') as outfile:
    json.dump(objData, outfile)
