from tkinter import *

root = Tk()

name = Entry(root,
      width=50,
      text="click Me!",
      fg="white",
      bg="gray")
name.pack()
name.insert(0, "Enter Your Name")

def myClick():
    Label(root, text="Hello " + name.get()).pack()


myButton = Button(root,
                  text="click Me!",
                  padx=50,
                  pady=15,
                  command=myClick,
                  fg="white",
                  bg="green").pack()
#Shoving it onto screen
root.mainloop()