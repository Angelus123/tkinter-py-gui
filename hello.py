from tkinter import *

root = Tk()
root.title("My  GUI")
root.geometry("300x200")
#creating a Label widget
myLabel = Label(root, text="Hello World")

#Shoving it onto screen
myLabel.pack()

root.mainloop()