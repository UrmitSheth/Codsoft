# Urmit_Sheth
# Task-3: Password generator 
from tkinter import *
import random, string  
import pyperclip

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("PassWord_Generator")

heading = Label(root, text='PASSWORD GENERATOR', font='arial 15 bold')
heading.pack()

Label(root, text='Thanks for coming', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold')
pass_label.pack()

pass_len = IntVar()
length = Spinbox(root, from_=8, to=32, textvariable=pass_len, width=15)
length.pack()

pass_str = StringVar()

def Generator():
    password = ''
    for _ in range(4):
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
    
    for _ in range(pass_len.get() - 4):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    pass_str.set(password)

Button(root, text="GENERATE PASSWORD", command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5)

root.mainloop()
