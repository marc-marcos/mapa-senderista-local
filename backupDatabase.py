import sys
import shutil


def restoreDatabase(path):
    shutil.copy2(path, "database.db")


def backupDatabase(path):
    shutil.copy2("database.db", path)


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
