from tkinter import *
from imaplib import *
from tkinter import ttk
from tkinter.ttk import *
  

def show():
    print("User Name :%s\nPassword :%s\nConfirm Password :%s\nFirst Name :%s\nLast Name :%s\nGender :%s\nPhone :%s\nEmail :%s\nAge :%s"%(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),var.get(),t6.get(),t7.get(),t8.get()))

top = Tk()

top.title("Registration from")
frame1 = ttk.Frame(top,padding =10)
frame1.grid()

label0 = ttk.Label(frame1, text='Registration Form',padding =(5,2),font="Time 16 bold",)
label0.grid(row = 0, columnspan=3, sticky = E,padx = 5, pady =5)

label1 = ttk.Label(frame1, text='User Name',padding=(5,2))
label1.grid(row = 1, column=0, sticky = E,padx = 5, pady =5)

label2 = ttk.Label(frame1, text='Password',padding=(5,2))
label2.grid(row=2, column=0, sticky=E,padx = 5, pady =5)

label3 = ttk.Label(frame1, text='Confirm Password',padding=(5,2))
label3.grid(row=3, column=0, sticky=E,padx = 5, pady =5)

label4 = ttk.Label(frame1, text='Frist Name',padding=(5,2))
label4.grid(row=4, column=0, sticky=E,padx = 5, pady =5)

label5 = ttk.Label(frame1, text='Last Name',padding=(5,2))
label5.grid(row=5, column=0, sticky=E,padx = 5, pady =5)

label6 = ttk.Label(frame1, text='Gender',padding=(5,2))
label6.grid(row=6, column=0, sticky=E,padx = 5, pady =5)

label7 = ttk.Label(frame1, text='Phone',padding=(5,2))
label7.grid(row=1,column=2, sticky=E,padx = 5, pady =5)
    
label8 = ttk.Label(frame1, text='Email',padding=(5,2))
label8.grid(row=2, column=2, sticky=E,padx = 5, pady =5)

label9 = ttk.Label(frame1, text='City',padding=(5,2))
label9.grid(row=3, column=2, sticky=E,padx = 5, pady =5)

label9 = ttk.Label(frame1, text='Age',padding=(5,2))
label9.grid(row=4, column=2, sticky=E,padx = 5, pady =5)

label10 = ttk.Label(frame1, text='Hobbies',padding=(5,2))
label10.grid(row=5, column=2, sticky=E,padx = 5, pady =5)

t1 = ttk.Entry(frame1,width = 30)
t1.grid(row = 1,column = 1)

t2 = ttk.Entry(frame1,width = 30)
t2.grid(row = 2,column = 1)

t3 = ttk.Entry(frame1,width = 30)
t3.grid(row = 3,column = 1)

t4 = ttk.Entry(frame1,width = 30)
t4.grid(row = 4,column = 1)

t5 = ttk.Entry(frame1,width = 30)
t5.grid(row = 5,column = 1)

t6 = ttk.Entry(frame1,width = 30)
t6.grid(row = 1,column = 3)
    
t7 = ttk.Entry(frame1,width = 30)
t7.grid(row = 2,column = 3)

t8 = ttk.Entry(frame1,width = 30)
t8.grid(row = 4,column = 3)

var=IntVar()
r1 = Radiobutton(frame1,text = 'Male',variable = var,value = 1,padding=(5,2))
r1.grid(row = 6, column =1,sticky=W)
r2 = Radiobutton(frame1,text = 'Female',variable = var,value = 2,padding =(5,2))
r2.grid(row = 6, column = 1)


combo = Combobox(frame1)
combo['values']=("Hyderabad","Bangalore","Chennai")
combo.grid(row = 3,column = 3,sticky = W)
combo.current(0)
         
lb = Listbox(frame1,width=20,height=4)
lb.insert(1,"Redding")
lb.insert(2,"Singging")
lb.insert(3,"Playing")
lb.insert(4,"Sleeping")
lb.grid(row=5, column = 3,sticky=W)


    
Button(frame1, text = 'Submit' ,command = show).grid(row = 7, columnspan = 3,padx=200)
top.mainloop()
