import os
import sqlite3

DATABASE = 'database.db'

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

c.execute('SELECT * FROM routes')
rows = c.fetchall()

print(f"Status  Name\n")
for row in rows:
    print(f"{row[2]}       {row[0]}")

option = "a"

while option != "exit":
    option = input("\nWhich route would you like to modify? (Enter the name of the route)\n")
    new_status = input("What would you like to change the status to? (0 = red, 1 = purple, 2 = green)\n")

    c.execute('UPDATE routes SET status=? WHERE route_path=?', (new_status, option))

conn.commit()
conn.close()