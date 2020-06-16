from tkinter import *

root = Tk()

def dosomething():
    print("You have clicked button")

button1 = Button(root, text="Click here", bg="Blue", fg="White", command=dosomething)
button1.pack()

root.mainloop()