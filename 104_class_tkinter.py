from tkinter import *

class MyButtons:

    #Creating an __init__ method

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printmessage = Button(frame, text="Click here", bg="Red", fg="White", command=self.printmessage)
        self.printmessage.pack()

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack()

    def printmessage(self):
        print("You have clicked button")
        

root = Tk()        
#This line will create an object of class MyButtons
object1 = MyButtons(root)

root.mainloop()
