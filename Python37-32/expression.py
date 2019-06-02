from tkinter import *
from tkinter import ttk
    
top = Tk()
top.title("Registration from")
top.resizable(False,False)
frame1 = ttk.Frame(top,padding = 10)
frame1.grid()

label1 = ttk.Label(frame1, text = 'Name',Padding = (5,2))
label1.grid(row = 0,column = 0 ,stiky = E)

label2 = ttk.Label(frame1, text = 'Password',Padding = (5,2))
label2.grid(row = 1,column = 0 ,stiky = E)


top.mainloop()
