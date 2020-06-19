from tkinter import *

#Import messagebox from tkinter module
import tkinter.messagebox

#This line will create a messagebox
message = tkinter.messagebox.showinfo("This is the title", "This is a message box")

#This line will create a question box
response = tkinter.messagebox.askquestion("Question 1", "Do you like coffee?")

if response == "yes":
    tkinter.messagebox.showinfo("Good news", "Here is some coffee for you")
