import os
import sys

if len(sys.argv) < 2:
    print("-r to restore the database\n-b to backup the database\n")

else:
    if (sys.argv[1] == "-r"):
        os.system("cp database.db.bak database.db")
        print("Database restored.")
    
    elif (sys.argv[1] == "-b"):
        os.system("cp database.db database.db.bak")
        print("Database backed up.")
    
    else:
        print("-r to restore the database\n-b to backup the database\n")