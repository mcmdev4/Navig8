import os
import shlex
import time
from tkinter import *
from tkinter import filedialog

print("Welcome to Navig8 LWVM Enviroment")

def env():

    while True:

        command = input("~ $ ")

        try:
            args = shlex.split(command)
        except Exception as e:
            raise e

        if command.strip().lower().startswith("print"):
            if len(args) > 1:
                print(" ".join(args[1:]))
        elif command.strip().lower().startswith("shutdown"):
            print("Shutting down...")
            time.sleep(5)
            break
        elif command.strip().lower().startswith("open"):
            if args[1] == "Postit":
                postit()
                pass
        else:
            print("Error: Command does not exist")


def postit():

    def saveFile():
        file = filedialog.asksaveasfile(defaultextension=".txt",
        filetypes=[
            ("Text file",".txt"),
            ("JSON file",".json"),
            ("All Files",".*")
        ])

        if file:
            content = str(text.get(1.0,END))
            file.write(content)
            file.close()
    
    def openFile():
        path = filedialog.askopenfilename(defaultextension=".txt",
        filetypes=[
            ("Text files",".txt"),
            ("JSON files",".json"),
            ("All files",".*")
        ])
        
        if path:
            with open(path, 'r') as c:
                content = c.read()
            text.delete(1.0,END)
            text.insert(1.0,content)

    window = Tk()
    window.title("Postit text editor")
    
    menubar = Menu(window)
    window.config(menu=menubar)

    filemenu = Menu(menubar)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Save as",command=saveFile)
    filemenu.add_command(label="Open",command=openFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quit)

    text = Text(window)

    text.pack()
    window.mainloop()



env()