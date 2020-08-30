import pandas as pd
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from io import BytesIO


class Equalizer():
    def __init__(self, spreadsheet=None, url=None):
        self.spreadsheet:pd.DataFrame = None
        if spreadsheet:
            self.spreadsheet = spreadsheet
        if url:
            req = requests.get(url)
            data_file = req.content
            spreadsheet = pd.read_csv(BytesIO(data_file))
            self.spreadsheet = spreadsheet
            print(self.spreadsheet.head())
            print("Data Loaded.")

    def init_spreadsheet(self):
        self.spreadsheet = pd.DataFrame()

    def add_member(self, member_name:str):
        self.spreadsheet.

    @staticmethod
    def fromDrive():
        gauth = GoogleAuth()
        # gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)

        file_list = drive.ListFile(
            {'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            print('title: %s, id: %s' % (file1['title'], file1['id']))
