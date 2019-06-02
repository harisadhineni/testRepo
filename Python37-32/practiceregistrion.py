from tkinter import *

def main_screen():
    screen = Tk()
    screen.geometry("350x250")
    screen.title("Registrion From")
    Label(text='Registration From', bg ="grey",width = "300", height ="2").pack()
    Label(text ='').pack
    Button(text="Login").pack()
    Button(text = "Register").pack()

    screen.mainloop()
main_screen()
    
