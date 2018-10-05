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
import httplib2
import ssl

coll = 123

file= open('cleanedData.txt' , 'r+')

with open('UK Makerspaces Research Survey (Public 2015-01-12).csv') as f:
    reader = csv.reader(f)
    for row in reader:

        domainName = row[3]
        print(domainName)
        if not row[3] == '':
            try:
                resp,content = httplib2.Http().request(domainName)

                if resp.status == '200':
                    print ('It Worked')
                else:
                    print ('Not worked')
                #file.write(str(domainName))

                """
                if '200' in resp:
                    file.write(str(domainName))
                else:
                    print("Website Closed")
                """
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



file.close()