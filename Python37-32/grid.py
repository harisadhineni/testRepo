from tkinter import *

def show():
    print("First Name : %s\nLastName : %s\nEmail :%s\nphone :%s"%(e1.get(),e2.get(),e3.get(),e4.get()))
top = Tk()
top.configure(background="yellow")

Label(top, text="First Name ").grid(row = 0)
Label(top, text="Last Name ").grid(row = 1)
Label(top, text="Email").grid(row = 2)
Label(top, text="phone").grid(row = 3)

e1 = Entry(top)
e2 = Entry(top)
e3 = Entry(top)
e4 = Entry(top)

e1.grid(row = 0,column = 1)
e2.grid(row = 1,column = 1)
e3.grid(row = 2,column = 1)
e4.grid(row = 3,column = 1)

Button(top, text = 'show' , command = show).grid(row = 4, column = 0, sticky = W, pady = 10)
Button(top, text = 'exit' , command = quit).grid(row =4,column =1,sticky = W,pady = 10)

top.mainloop()
