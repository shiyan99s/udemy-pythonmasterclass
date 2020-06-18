from tkinter import *

root = Tk()

def add(x,y):
    print(x+y) 

def sub(x,y):
    print(x-y)

def div(x,y):
    print(x//y)

def mul(x,y):
    print(x*y)

title1 = Label(root, text="Welcome to Shiyan's cal", bg="Red", fg="White")
title1.pack()

label1 = Label(root, text="Enter X")
label2 = Label(root, text="Enter Y")

entryx = Entry(root)
entryy = Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=0, column=0)

entryx.grid(row=0, column=1)
entryy.grid(row=1, column=1)

button1 = Button(root, text="Add", command=add)
button2 = Button(root, text="Sub", command=sub)
button3 = Button(root, text="Div", command=div)
button4 = Button(root, text="Mul", command=mul)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

root.mainloop()