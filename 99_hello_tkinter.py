#99_hello_tkinter.py
from tkinter import *

root = Tk()

label1 = Label(root, text="Hello Tkinter")
label2 = Label(root, text="VSCode")
label1.pack()
label2.pack()

root.mainloop()