#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12rhodesd
#
# Created:     05/10/2018
# Copyright:   (c) 12rhodesd 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import os
import httplib

coll = 123

with open('UK Makerspaces Research Survey (Public 2015-01-12).csv') as f:
    reader = csv.reader(f)
    for row in reader:

        row3 = row[3]
        splitRow3 = row3[7:]

        try:
            connected = httplib.HTTPConnection(splitRow3)
            connected.connect()
            row[coll] = 'Exists'
        except:
            row[coll] = 'Doesnt Exist'

        """if (response == 0):
            print (row[3])
            row[coll] = 'exists'

        else:
            row[coll] = 'Doesnt Exist'
        """
        print(row)
