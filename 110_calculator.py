#Calculator

from tkinter import *
# Importing parser
import parser

root = Tk()

# Get the user input and display in the text field
i = 0
def get_variables(num):
    global i
    # Adding variables to entry field, i.e display using insert module
    display.insert(i, num)
    i += 1


# Creating function for ALL CLEAR (AC)
def clear_all():
    display.delete(0, END)


# Creating function for delete button
def delete_function():
    # Creating a new variable to store the number in text field 
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "ERROR")


# Creating function for adding input & operators on display
def display_operators(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# Creating function for "=" sign
def calculate():
    entire_string = display.get()
    try:
        # Creating a variable where parser will calculate the expression(expr) and compile()
        var = parser.expr(entire_string).compile()
        result = eval(var)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "SYNTAX ERROR")


# Creating function for factorial
def factorial():
    # Creating a variable to get string from text field
    variable = display.get()
    variable = int(variable)
    # Code for factorial
    f = 1
    for i in range(1, variable+1):
        f = f*i
    # Clearing text field and printing factorial in text field
    clear_all()
    display.insert(0, f)

root.title("Calculator")

# Adding the input field
display = Entry(root)
display.grid(row=1, columnspan=7, sticky=W+E)

# Adding buttons to the calculator
Button(root, text="7", command = lambda: get_variables(7)).grid(row=2, column=0)
Button(root, text="8", command = lambda: get_variables(8)).grid(row=2, column=1)
Button(root, text="9", command = lambda: get_variables(9)).grid(row=2, column=2)

Button(root, text="4", command = lambda: get_variables(4)).grid(row=3, column=0)
Button(root, text="5", command = lambda: get_variables(5)).grid(row=3, column=1)
Button(root, text="6", command = lambda: get_variables(6)).grid(row=3, column=2)

Button(root, text="1", command = lambda: get_variables(1)).grid(row=4, column=0)
Button(root, text="2", command = lambda: get_variables(2)).grid(row=4, column=1)
Button(root, text="3", command = lambda: get_variables(3)).grid(row=4, column=2)

# Adding the extra buttons
Button(root, text="AC", command = lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", command = lambda: get_variables(0)).grid(row=5, column=1)
Button(root, text="=", command = lambda : calculate()).grid(row=5, column=2)

# Adding mathematical operators
Button(root, text="+", command = lambda : display_operators("+")).grid(row=2, column=4)
Button(root, text="-", command = lambda : display_operators("-")).grid(row=3, column=4)
Button(root, text="*", command = lambda : display_operators("*")).grid(row=4, column=4)
Button(root, text="/", command = lambda : display_operators("/")).grid(row=5, column=4)

# Adding the advance operators, column 5
Button(root, text="pi", command = lambda : display_operators("*3.14")).grid(row=2, column=5)
Button(root, text="%", command = lambda : display_operators("%")).grid(row=3, column=5)
Button(root, text="(", command = lambda : display_operators("(")).grid(row=4, column=5)
Button(root, text="exp", command = lambda : display_operators("**")).grid(row=5, column=5)

# Adding more advance operators, column 6
Button(root, text="<-", command = lambda: delete_function()).grid(row=2, column=6)
Button(root, text="x!", command = lambda : factorial()).grid(row=3, column=6)
Button(root, text=")", command = lambda : display_operators(")")).grid(row=4, column=6)
Button(root, text="x^2", command = lambda : display_operators("**2")).grid(row=5, column=6)

root.mainloop()