from tkinter import Tk, Button, Text
from tkinter import filedialog as fd
import webbrowser

from backup_and_restore_gui import backup_and_restore_gui
from startupMap import startupMap
from regenerateRoutes import regenerateRoutes
from modifyDatabase import modifyDatabase


def gui():
    window = Tk()
    window.title("Mapa Senderista Local")

    btn = Button(window, text="Startup Map", command=startupMap)
    btn.pack()

    btn3 = Button(window, text="Open Map",
                  command=lambda: webbrowser.open('index.html'))
    btn3.pack()

    btn2 = Button(window, text="Regenerate Routes", command=regenerateRoutes)
    btn2.pack()

    btn4 = Button(window, text="Backup/Restore Database",
                  command=backup_and_restore_gui)
    btn4.pack()

    btn7 = Button(window, text="Modify Status", command=gui_modifyStatus)
    btn7.pack()

    btn6 = Button(window, text="Exit", command=window.destroy)
    btn6.pack()

    window.mainloop()


def modifyStatusAndClose(file_path, status, window):
    modifyDatabase(file_path, status)
    window.destroy()


def gui_modifyStatus():
    filename = fd.askopenfilename()

    file_path = filename.split('/')[-1]

    window = Tk()
    window.title("Modify Status")

    inputtxt = Text(window, height=1, width=20)
    inputtxt.pack()

    btn = Button(window, text="To-Do",
                 command=lambda: modifyStatusAndClose(file_path, 0, window))
    btn.pack()

    btn2 = Button(window, text="Planned",
                  command=lambda: modifyStatusAndClose(file_path, 1, window))
    btn2.pack()

    btn3 = Button(window, text="Done",
                  command=lambda: modifyStatusAndClose(file_path, 2, window))
    btn3.pack()

    window.mainloop()
