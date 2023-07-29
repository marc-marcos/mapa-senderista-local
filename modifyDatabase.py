import os
import sqlite3

def modify_database(route, status):
    DATABASE = 'database.db'

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('UPDATE routes SET status=? WHERE route_path=?', (status, route))

    conn.commit()
    conn.close()

if __name__ == "__main__":
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

        modify_database(option, new_status)

    conn.commit()
    conn.close()