from tkinter import *

def function1():
    print("File menu clicked")

def function2():
    print("Edit menu clicked")

def function3():
    print("You have clicked toolbar button")

root = Tk()

#This line will create an object of an pre-existing class Menu
mymenu = Menu(root)

#This line is telling that this is my main menu and we'll be working on it
root.config(menu=mymenu)

#This will create submenu in main menu
submenu = Menu(mymenu)
submenu1 = Menu(mymenu)

#This line will assign submenu under main menu
mymenu.add_cascade(label="File", menu=submenu)
mymenu.add_cascade(label="Edit", menu=submenu1)

#This line will add items to submenu
submenu.add_command(label="New File", command=function1)
submenu.add_command(label="New Window", command=function1)
submenu.add_command(label="Open File", command=function1)

submenu1.add_command(label="Undo", command=function2)
submenu1.add_command(label="Redo", command=function2)
submenu1.add_command(label="Cut", command=function2)

#This line will create a toolbar
toolbar1 = Frame(root, bg="pink")
button1 = Button(toolbar1, text="Save as PDF", command=function3)
button1.pack(side=LEFT, padx=2, pady=3)

button2 = Button(toolbar1, text="Print PDF", command=function3)
button2.pack(side=LEFT, padx=4, pady=4)

button3 = Button(toolbar1, text="Exit", command=toolbar1.quit)
button3.pack(side=LEFT, padx=4, pady=4)

toolbar1.pack(side=TOP, fill=X)

root.mainloop()