from tkinter import *

top = Tk()

def fun1():
    label1 =Label(top, text = "harikrishna",command = fun1,padding = (5,2))
    top.grid()
    top.mainloop()
