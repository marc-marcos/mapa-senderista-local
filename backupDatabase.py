import os
import sys

def restoreDatabase():
    os.system("cp database.db.bak database.db")
    print("Database restored.")

def backupDatabase():
    os.system("cp database.db database.db.bak")
    print("Database backed up.")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("-r to restore the database\n-b to backup the database\n")

    else:
        if (sys.argv[1] == "-r"):
            restoreDatabase()
        
        elif (sys.argv[1] == "-b"):
            backupDatabase()
        
        else:
            print("-r to restore the database\n-b to backup the database\n")