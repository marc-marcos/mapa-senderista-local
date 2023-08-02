import folium
import webbrowser
import gpxpy
import sqlite3
import os

from creatingDatabase import createDatabase 
from gui import gui
from gui import gui_modifyStatus

if __name__ == "__main__":
    # If the database doesn't exist, create it
    DATABASE = 'database.db'

    if not os.path.exists(DATABASE):
        createDatabase()
    
    gui()