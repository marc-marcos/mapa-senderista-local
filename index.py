import os

from src.creatingDatabase import createDatabase 
from src.gui import gui

if __name__ == "__main__":
    # If the database doesn't exist, create it
    DATABASE = 'database.db'

    if not os.path.exists(DATABASE):
        createDatabase()
    
    gui()