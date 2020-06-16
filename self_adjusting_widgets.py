from tkinter import *

root = Tk()

label1 = Label(root, text="X,horizontal", bg="Blue", fg="White")
label2 = Label(root, text="Y,vertical", bg="Red", fg="White")

label1.pack(fill=X)
label2.pack(side=LEFT, fill=Y)

root.mainloop()