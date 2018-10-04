#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12rhodesd
#
# Created:     03/10/2018
# Copyright:   (c) 12rhodesd 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import urllib

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    index = 2

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    SPREADSHEET_ID = '1vPS7onHZKN3PcVgIfP6fmlmXZelPaKGXwFBL5fKt3d4'
    RANGE_NAME = 'D2:DT'
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                                range=RANGE_NAME).execute()
    values = result.get('values', [])


    service = discovery.build('sheets', 'v4', credentials=creds)

    batch_update_spreadsheet_request_body = {
       "requests": [
        {
        "deleteDimension": {
            "range": {
           "sheetId": SPREADSHEET_ID,
           "dimension": "ROWS",
           "startIndex": 2,
           "endIndex": 2
           }
       }
       },
       ]
   }

    if not values:
        print('No data found.')
    else:
        print('URL:')
        for row in values:
            try:
                print(row[1])
                print(index)
            except:
                print('error')
                #request = service.spreadsheets().batchUpdate(SPREADSHEET_ID, body=batch_update_spreadsheet_request_body)
            index = index + 1




if __name__ == '__main__':
   main()