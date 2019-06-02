from tkinter import *
v = IntVar()

Radiobutton(root, text="Red", variable=v, value=1, command = red).grid(row=1) 
Radiobutton(root, text="Blue", variable=v, value=2, command = blue).grid(row=2)
Radiobutton(root, text="Green", variable=v, value=3, command = green).grid(row=3)
Radiobutton(root, text="Other", variable=v, value=4, command = Other).grid(row=4)
