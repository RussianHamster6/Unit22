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
from httplib2 import Http
from oauth2client import file, client, tools
import gspread
import urllib

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
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

    if not values:
        print('No data found.')
    else:
        print('URL:')
        for row in values:
            try:
                print(row[3])
            except:
                sheet.delete_row(row)


if __name__ == '__main__':
   main()