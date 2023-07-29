import os
import sqlite3

def modifyLink(route, link):
    DATABASE = 'database.db'

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('UPDATE routes SET link=? WHERE route_path=?', (link, route))

    c.close()
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
        link = input("What is the link of the route?\n")

        modifyLink(option, link)

    conn.commit()
    conn.close()