# API do Google(Planilha)
from __future__ import print_function
import httplib2
import os
import datetime
import csv
import sys
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser (parents=[tools.argparser]).parse_args ()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser ('~')
    credential_dir = os.path.join (home_dir, '.credentials')
    if not os.path.exists (credential_dir):
        os.makedirs (credential_dir)
    credential_path = os.path.join (credential_dir,
                                    'sheets.googleapis.com-python-quickstart.json')

    store = Storage (credential_path)
    credentials = store.get ()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets (CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow (flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run (flow, store)
        print ('Storing credentials to ' + credential_path)
    return credentials


def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials ()
    http = credentials.authorize (httplib2.Http ())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build ('sheets', 'v4', http=http,
                               discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1PUUCb8TtlKnoJdd8qaTvAZVM476fNuJedvp6BEdJedY'
    rangeName = 'Burnup Chart - #SP1706!F34:I59'
    result = service.spreadsheets ().values ().get (
        spreadsheetId=spreadsheetId, range=rangeName).execute ()
    values = result.get ('values', [])

    if not values:
        print ('No data found.')
    else:
        # TODO linhas 76 e 77 fazem a impressão da data de hoje no sistema

        d1 = int(datetime.date.today ())

        print (d1)

        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print ('%s, %s' % (row[0], row[1]))
            
            # TODO Envio de email ao encontrar uma data igual a data do sistema e, que a coluna de Realizado estiver vazio (Em construção)

            # TODO Salvar o resultado em formato .csv

if __name__ == '__main__':
    main ()
