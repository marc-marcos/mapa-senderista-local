from tkinter import *
from tkinter import filedialog as fd

from src.backupDatabase import backupDatabase, restoreDatabase
from src.generate_path_backup import generate_path_backup


def backup_and_restore_gui():
    window = Tk()
    window.title("Backup and Restore database")

    btn = Button(window, text="Backup Database",
                 command=lambda: backupDatabase(generate_path_backup()))
    btn.pack()

    btn2 = Button(window, text="Restore Database",
                  command=lambda: restoreProcess(window))
    btn2.pack()

    window.mainloop()


def restoreProcess(window):
    filename = fd.askopenfilename()
    restoreDatabase(filename)

    window.destroy()
