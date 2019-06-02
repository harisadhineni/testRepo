from tkinter import *
from tkinter import ttk

def main_screen():
    top = Tk()
    top.title("Login from")
    top.resizable(False,False)
    frame1 = ttk.Frame(top,padding = 10)
    frame1.grid()

    label1 = Label(frame1, name = "username", padding = (5,2)).grid(row=0, column=0, sticky=E)
    label2 = Label(frame1, name = "email", padding = (5,2)).grid(row=1, column=0, sticky=E)

    t1 = ttk.Entry(frame1, width = 30).grid(row=0, column=1)
    t2 = ttk.Entry(frame1, width = 30).grid(row=1, column=1)
    t3 = ttk.Entry(frame1, width = 30).grid(row=2, column=1)

    frame2 = ttk.Frame(frame1, padding = (0,5)).grid(row=3, column=1, sticky=W)

    button1 = ttk.Button(frame2, text="OK").pack(side=LEFT)
    button2 = ttk.Button(frame2, text="cancel",command=quit).pack(side=LEFT)
    
                       

    top.mainloop()
    
main_screen()
