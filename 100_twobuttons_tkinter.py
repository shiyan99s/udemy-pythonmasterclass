#Tkinter 100_twobuttons.py

from tkinter import *
#This line will create the main window
root = Tk()
#These two lines will create the frames for the buttons
frame1 = Frame(root)
frame2 = Frame(root)
#These two lines will pack the frames in windows acc. to placement assigned
frame1.pack()
frame2.pack(side=BOTTOM)
#These two lines will create buttons, assign text, assign color
button1 = Button(frame1, text="1.click here", fg="Red")
button2 = Button(frame2, text="2.click here", fg="Blue")
#These two lines will pack the buttons to the main window
button1.pack()
button2.pack()
#This line will keep loop the window untill the user closes the window
root.mainloop()