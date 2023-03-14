from tkinter import *

root = Tk()


def myClick():
    Label(root, text="Look! I have clicked a button").pack()


myButton = Button(root,
                  text="click Me!",
                  padx=50,
                  pady=15,
                  command=myClick,
                  fg="white",
                  bg="green").pack()
#Shoving it onto screen
root.mainloop()