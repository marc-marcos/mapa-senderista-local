import sqlite3
import gpxpy
import gpxpy.gpx
import os

DATABASE = 'database.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

dir_path = 'routes/'

# If a route is in the database but not in the folder, delete it
for row in cursor.execute('SELECT * FROM routes'):
    if row[0] not in os.listdir(dir_path):
        cursor.execute('DELETE FROM routes WHERE route_path=?', (row[0],))

for path in os.listdir(dir_path):
    if path.endswith('.gpx'):
        print(path)
        name = str(path).split('.')[0]

        # If a route with the same path already exists, skip this one
        if cursor.execute('SELECT * FROM routes WHERE route_path=?', (str(path),)).fetchone() is None:
            cursor.execute('INSERT INTO routes (route_path, route_name, status) VALUES (?, ?, ?)', (str(path), name, 0))

cursor.close()
conn.commit()
conn.close()