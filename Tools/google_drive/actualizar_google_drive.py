import pandas as pd
import gspread
import os
from pathlib import Path
from google.oauth2.service_account import Credentials
#Librerias Propias
from config import config

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

def actualizar_google_drive(sample_spreadsheet_id, name_worksheet,lst_columns,lst_values):
    # Link to authenticate 
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]

    credentials = Credentials.from_service_account_file(
            config.llave_json,
            scopes=scopes
        )
    
    # Request authorization and open the selected spreadsheet
    gc = gspread.authorize(credentials).open_by_key(sample_spreadsheet_id)
    #WorkSheet
    worksheet=gc.worksheet(name_worksheet)
    next_row = next_available_row(worksheet)
    #Update
    for index,item in enumerate(lst_columns):
        worksheet.update_cell(next_row,item,lst_values[index])