import pandas as pd
import gspread
import os
from pathlib import Path
from google.oauth2.service_account import Credentials


def get_data_google_sheets(sample_spreadsheet_id, name_worksheet):
    
    # Link to authenticate 
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]
    ruta_json = os.path.dirname(os.path.dirname(__file__))

    #llave_json = r'C:\Users\Excelentia\Google Drive\00. Empresa\08. RPA\00.RPA_Excelentia\tools\llave.json'
    llave_json = r'{}\tools\llave.json'.format(ruta_json)
    # Read the .json file and authenticate with the links
    credentials = Credentials.from_service_account_file(
            llave_json,
            scopes=scopes
        )
    
    # Request authorization and open the selected spreadsheet
    gc = gspread.authorize(credentials).open_by_key(sample_spreadsheet_id)

    # Prompts for all spreadsheet values
    #values = gc.get_worksheet(tab_index).get_all_values()
    values = gc.values_get(name_worksheet)
    # Turns the return into a dataframe
    df = pd.DataFrame(values['values'])
    df.columns = df.iloc[0]
    df.drop(df.index[0], inplace=True)

    return df