from tkinter import *

def function():
    print("Menu item clicked")

root = Tk()

mainmenu = Menu(root)
root.config(menu=mainmenu)

submenu = Menu(mainmenu)
submenu2 = Menu(mainmenu)
submenu3 = Menu(mainmenu)
submenu4 = Menu(mainmenu)
submenu5 = Menu(mainmenu)
submenu6 = Menu(mainmenu)
submenu7 = Menu(mainmenu)
submenu8 = Menu(mainmenu)



mainmenu.add_cascade(label="File", menu=submenu)
mainmenu.add_cascade(label="Edit", menu=submenu2)
mainmenu.add_cascade(label="Selection", menu=submenu3)
mainmenu.add_cascade(label="View", menu=submenu4)
mainmenu.add_cascade(label="Go", menu=submenu5)
mainmenu.add_cascade(label="Run", menu=submenu6)
mainmenu.add_cascade(label="Terminal", menu=submenu7)
mainmenu.add_cascade(label="Help", menu=submenu8)

#SUBMENU FOR FILE MENU
submenu.add_command(label="New File", command=function)
submenu.add_command(label="New Window", command=function)
submenu.add_command(label="Open File", command=function)
submenu.add_command(label="Open Folder", command=function)
submenu.add_command(label="Open Workspace", command=function)
submenu.add_command(label="Open Recent", command=function)
submenu.add_command(label="Add Folder to Workspace", command=function)
submenu.add_command(label="Save Workspace As", command=function)
submenu.add_command(label="Save As", command=function)
submenu.add_command(label="Save All", command=function)
submenu.add_command(label="Auto Save", command=function)
submenu.add_command(label="Preferences", command=function)
submenu.add_command(label="Revert File", command=function)
submenu.add_command(label="Close Editor", command=function)
submenu.add_command(label="Close Folder", command=function)
submenu.add_command(label="Close Window", command=function)
submenu.add_command(label="Exit", command=function)

#SUBMENU FOR EDIT MENU

submenu2.add_command(label="Undo", command=function)
submenu2.add_command(label="Redo", command=function)
submenu2.add_command(label="Copy", command=function)
submenu2.add_command(label="Paste", command=function)
submenu2.add_command(label="Find", command=function)
submenu2.add_command(label="Replace", command=function)
submenu2.add_command(label="Find in Files", command=function)
submenu2.add_command(label="Replace in Files", command=function)
submenu2.add_command(label="Toggle Line Comment", command=function)
submenu2.add_command(label="Toggle Block Comment", command=function)
submenu2.add_command(label="Emmet: Expand Abbreviation", command=function)
submenu2.add_command(label="Emment", command=function)



root.mainloop()