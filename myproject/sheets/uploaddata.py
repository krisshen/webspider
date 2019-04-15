import os.path
import pickle
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GoogleDrive():
    
    def __init__(self):
        print("init Google api")
        SCOPES = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive.metadata",
                "https://www.googleapis.com/auth/drive.file"
                ]
        
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'quickstart/credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.sheetService = build('sheets', 'v4', credentials=creds)
        self.fileService = build('drive', 'v3', credentials=creds)

    def createSheet(self, title):
        print("create new sheet")
        sheetService = self.sheetService
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = sheetService.spreadsheets().create(body=spreadsheet,
                                            fields='spreadsheetId').execute()
        print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
        # [END sheets_create]
        return spreadsheet.get('spreadsheetId')

    def moveFile(self, file_id):
        self.Google_Folder_ID = "1xGdQ5u2SbsmYNKzqQgcJ41lp2y43ADAH"
        self.file = self.fileService.files().get(fileId=file_id, fields='parents').execute()
        self.previousParents = ",".join(self.file.get('parents'))
        self.file = self.fileService.files().update(fileId=file_id,
                                                    addParents=self.Google_Folder_ID,
                                                    removeParents=self.previousParents,
                                                    fields='id, parents').execute()

    def listFiles(self):
        results = self.fileService.files().list(q="'1Ec7rwK1VmdZhSKSdJ-7CTVVqqp9sR3bc' in parents").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))

def getCurrentDate():
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    print("get current date: ", now)
    return now

def main():
    print("uploaddata.main")
    googleDrive = GoogleDrive()
    date = getCurrentDate()
    sheetId = googleDrive.createSheet(date)
    googleDrive.moveFile(sheetId)
    

if __name__ == '__main__':
    main()