#-------------------------------------------------------------------------------
# Name:        DataCleaning
# Purpose:
#
# Author:      Declan Rhodes
#
# Created:     05/10/2018
# Copyright:   (c) Declan Rhodes 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv
import os
import httplib2
import ssl
import sys

coll = 123

header = True

f = open('UK Makerspaces Research Survey (Public 2015-01-12).csv')
reader = csv.reader(f)
with open('cleanedData.csv', 'w') as newF:
    writer = csv.writer(newF, delimiter=',')
    for row in reader:

        if (header == True) :
            writer.writerow([row[0],row[2],row[3],row[12]])
            header = False

        domainName = row[3]
        print(domainName)
        if not row[3] == '':
            try:
                resp,content = httplib2.Http().request(domainName)

                if resp.status == 200:
                    writer.writerow([row[0],row[2],row[3],row[12]])
                else:
                    print ('Website Connection Error')

            except httplib2.RelativeURIError:
                print ('not absolute url')
            except ssl.SSLError:
                print("Failed Connection")
            except httplib2.ServerNotFoundError:
                print('Server not found')
            except httplib2.RedirectLimit:
                print ('Redirect Limit Reached')
        else:
            print("No Webpage")


newF.close()