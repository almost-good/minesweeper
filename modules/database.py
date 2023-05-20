"""
Database

Database set up.

Connects to database.

Important for version 2.
"""

import gspread
from google.oauth2.service_account import Credentials


# Set up database
SCOPE = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("minesweeper-db")

# IMPORTANT FOR VERSION 2