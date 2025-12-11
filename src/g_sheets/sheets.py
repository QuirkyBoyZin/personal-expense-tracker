## comment when testing

from . import modify 
from . import retrieve
import time
## uncomment when testing

# import modify
# import retrieve

import os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service_account_file = "credential.json"
creds = Credentials.from_service_account_file(service_account_file, scopes=SCOPES)
sheet_id = os.getenv("SHEET_ID")
client = gspread.authorize(creds)
SHEET_GID = 0  # change if your tab has a different gid
DATA_RANGE = "A2:F"
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
workbook = client.open_by_key(sheet_id)
sheet_gspread = workbook.worksheet("Sheet1")
def measure_perf(base_fn):
    """A decorator for measuring code execution time of a function"""
    def wrapper(*args):
        
        start_time   = time.perf_counter()
        result = base_fn(*args)
        end_time     = time.perf_counter()
        elasped_time = end_time - start_time
        
        print(f"Execution time for {base_fn.__name__}: {elasped_time:.3f} Seconds")
        return result
       
    return wrapper
# Modifying data: add, update, remove

@measure_perf
def add_row(category: str, name: str, price: float):
    modify.add_row(sheet_gspread, category, name, price)

def remove_row(id: int):
    modify.remove_row(sheet_gspread, id)

def change_row(id: int, new_type = None, new_name = None, new_price = None ):
    modify.update_row(sheet_gspread, id, new_type,  new_name, new_price )

# Retrieving data

def get_all_expenses() -> list:
    return retrieve.retrieve_items(sheet, sheet_id, DATA_RANGE)

def get_expenses_at(date: str) -> list: 
    return retrieve.get_data(date, sheet, sheet_id, DATA_RANGE)
    
def get_item(id: int):
    return retrieve.get_item(id, sheet, sheet_id, DATA_RANGE)


if __name__ == "__main__":
    pass