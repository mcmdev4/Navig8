import os
import shlex
import time
from tkinter import *
from tkinter import filedialog
import runpy as rpy

print("Welcome to Navig8 LWVM Enviroment")

def env():

    while True:

        command = input("~ $ ")

        try:
            args = shlex.split(command)
        except Exception as e:
            print("Failed to run command")

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
            elif args[1] == "Magicalc":
                magicalc()
                pass
            else:
                print("invalid argument")
        elif command.strip().startswith("exepy"):
            rpy.run_path(args[1])
            pass
        elif command.strip().lower().startswith("choc"):
            print(f"Installing app: {args[1]}")

            result = subprocess.run(
                ["choco", "install", args[1], "-y"],
                capture_output=True,
                text=True,
            )

            print(result.stdout)

            if result.returncode == 0:
                print(f"Successfully installed app: {args[1]}")
            else:
                print(f"Failed to install app: {args[1]}")
                print(result.stderr)
        elif command.strip().lower().startswith("listaction"):
            if args[1].lower() == "command":
                print("""

                listaction: lists actions (commands, programs, etc.)

                print: prints an output from the first argument (args[1])

                shutdown: shuts down Navig8

                open: opens a graphical application

                exepy: executes a python script specified with the path (use it at your own risk)

                choc: installs an application to the computer via chocolatey (use it at your own risk)

                """)
            elif args[1] == "programs":
                print("""
                
                Magicalc: calculator

                Postit: notepad

                """)
            else:
                print("invalid argument")
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
    filemenu.add_command(label="Exit",command=window.destroy)

    text = Text(window)

    text.pack()
    window.mainloop()

def magicalc():
    global equation_text
    equation_text = ""
    

    def button_press(num):

        global equation_text

        equation_text = equation_text + str(num)

        equation_label.set(equation_text)

    def equals():

        global equation_text

        try:

            total = str(eval(equation_text))

            equation_label.set(total)

            equation_text = total

        except SyntaxError:

            equation_label.set("syntax error")

            equation_text = ""

        except ZeroDivisionError:

            equation_label.set("arithmetic error")

            equation_text = ""

    def clear():

        global equation_text

        equation_label.set("")

        equation_text = ""


    window = Tk()
    window.title("magicalc")
    window.geometry("300x300")

    equation_text = ""

    equation_label = StringVar()

    label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
    label.pack()

    frame = Frame(window)
    frame.pack()

    button1 = Button(frame, text=1, height=4, width=9, font=35,
                    command=lambda: button_press(1))
    button1.grid(row=0, column=0)

    button2 = Button(frame, text=2, height=4, width=9, font=35,
                    command=lambda: button_press(2))
    button2.grid(row=0, column=1)

    button3 = Button(frame, text=3, height=4, width=9, font=35,
                    command=lambda: button_press(3))
    button3.grid(row=0, column=2)

    button4 = Button(frame, text=4, height=4, width=9, font=35,
                    command=lambda: button_press(4))
    button4.grid(row=1, column=0)

    button5 = Button(frame, text=5, height=4, width=9, font=35,
                    command=lambda: button_press(5))
    button5.grid(row=1, column=1)

    button6 = Button(frame, text=6, height=4, width=9, font=35,
                    command=lambda: button_press(6))
    button6.grid(row=1, column=2)

    button7 = Button(frame, text=7, height=4, width=9, font=35,
                    command=lambda: button_press(7))
    button7.grid(row=2, column=0)

    button8 = Button(frame, text=8, height=4, width=9, font=35,
                    command=lambda: button_press(8))
    button8.grid(row=2, column=1)

    button9 = Button(frame, text=9, height=4, width=9, font=35,
                    command=lambda: button_press(9))
    button9.grid(row=2, column=2)

    button0 = Button(frame, text=0, height=4, width=9, font=35,
                    command=lambda: button_press(0))
    button0.grid(row=3, column=0)

    plus = Button(frame, text='+', height=4, width=9, font=35,
                    command=lambda: button_press('+'))
    plus.grid(row=0, column=3)

    minus = Button(frame, text='-', height=4, width=9, font=35,
                    command=lambda: button_press('-'))
    minus.grid(row=1, column=3)

    multiply = Button(frame, text='*', height=4, width=9, font=35,
                    command=lambda: button_press('*'))
    multiply.grid(row=2, column=3)

    divide = Button(frame, text='/', height=4, width=9, font=35,
                    command=lambda: button_press('/'))
    divide.grid(row=3, column=3)

    equal = Button(frame, text='=', height=4, width=9, font=35,
                    command=equals)
    equal.grid(row=3, column=2)

    decimal = Button(frame, text='.', height=4, width=9, font=35,
                    command=lambda: button_press('.'))
    decimal.grid(row=3, column=1)

    clear = Button(window, text='clear', height=4, width=12, font=35,
                    command=clear)
    clear.pack()

    window.mainloop()





env()