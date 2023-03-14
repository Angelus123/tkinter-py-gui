from tkinter import *
root = Tk()
root.title("My  Profile")
root.geometry("300x200")
#creating a Label widget
myLabel1 = Label(root, text="I am Felix").grid(row=0, column=0)
myLabel2 = Label(root, text="A software developer").grid(row=1, column=0)
myButton = Button(root, text="Go to My Protofolios!", padx=50, pady=30).pack()
root.mainloop()