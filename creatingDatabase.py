import os
import sqlite3

def createDatabase():
    DATABASE = 'database.db'

    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()

        c.execute('CREATE TABLE routes (route_path VARCHAR(255), route_name VARCHAR(100), status INT NOT NULL, link VARCHAR(255), PRIMARY KEY (route_path))')

        c.close()
        conn.commit()
        conn.close()

if __name__ == "__main__":
    createDatabase()