from tkinter import *

class MyButtons:

    #def __init__ method
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click here", command=self.printmessage)
        self.printbutton.pack()

        self.button1 = Button(frame, text="Quit", command=frame.quit)
        self.button1.pack(side=LEFT)

    def printmessage(self):
        print("You have clicked")


root = Tk()
#This line creates an object for MyButton class and passing root as the argument
object1 = MyButtons(root)

root.mainloop()