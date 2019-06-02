from tkinter import *
top = Tk()
top.title("win1")
top.geometry("350 x 200")

lb = Listbox(top)
lb.insert(1,"python")
lb.insert(2,"c language")
lb.insert(3,"ruby")
lb.pack()

top.mainloop()



