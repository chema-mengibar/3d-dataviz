import os
from os import listdir
from os.path import isfile, join
from math import cos, sin, pi

import sys
import json
import csv

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
geo.setEarthRadius( 4 )
# geo.scaleEarthRadius( 1000 )

'''
Countries Data : https://github.com/mledoze/countries
Download the repository a set the path
'''
# countries = []
# with open( currentDir + "/../../_docu/3d-data_geo/countries-master/countries.json") as f:
#     countriesFile = json.load(f)
#     for idc, c in enumerate( countriesFile):
#         countryPrefix = c["cca3"].lower()
#         countryFilePath = currentDir + "/../../_docu/3d-data_geo/countries-master/data/" + countryPrefix + ".geo.json"
#         if os.path.isfile( countryFilePath ):
#             print( "country ", countryPrefix, " exist"  )
#             countries.append( { "cursor": idc, "prefix": countryPrefix , "name":c["name"]["common"] } )
#         else:
#             print( "country ", countryPrefix, " doesn`t exist"  )
#
# print( countries )
# with open( currentDir + '/datasets/countries.json', 'w') as outfile:
#     json.dump(countries, outfile)
#


with open( currentDir + "/datasets/countries.json") as f:
    countries = json.load(f)


# cursors = [ 71,72,73,76,79,80,81,83,84,85,87,88,89,90,94,95,96,97,99,100  ]

for cursor, kk in enumerate( countries ):
# if True:
#     cursor = 105
# for cursor in cursors:

    error = False

    country = countries[ cursor ]

    countryPrefix = country["prefix"] # esp
    countryName = country["name"] # esp
    countryCursor = country["cursor"] # esp

    type = '' # Polygon or MultiPolygon

    with open( currentDir + "/../../_docu/3d-data_geo/countries-master/data/" + countryPrefix + ".geo.json") as f:
        jsonFile = json.load(f)
        if "geometry" in jsonFile["features"][0]:
            coordinates = jsonFile["features"][0]["geometry"]["coordinates"]
            type = jsonFile["features"][0]["geometry"]["type"]
        else:
            print( ">> error ", countryPrefix, countryName, cursor )
            error = True

    # Collect and transform coordinates
    if error == False:
        print( ">> drawing ", countryPrefix, countryName, countryCursor )
        nData = []
        if type == 'MultiPolygon':
            for d in coordinates:
                for e in d:
                    buffer = []
                    for f in e:
                        xyz = geo.coorToXyz( f[0], f[1], 0 )
                        buffer.append( xyz )
                    nData.append( buffer )

        elif type == 'Polygon':
            for d in coordinates:
                buffer = []
                for e in d:
                    xyz = geo.coorToXyz( e[0], e[1], 0 )
                    buffer.append( xyz )
                nData.append( buffer )

        # Draw
        for nd in nData:
            aConfig = {
                'type':'triangle',
                'name': 'country_' + countryPrefix,
                'verts': nd,
                'material': 'tres'
            }
            creator = Creator( aConfig )
