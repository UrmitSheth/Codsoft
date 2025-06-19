import tkinter
from tkinter import *
from tkinter.messagebox import showerror
import math

def add_text(text, strvar: StringVar):
    strvar.set(f'{strvar.get()}{text}')

def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        strvar.set(f"{strvar.get()}={eval(operation)}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')

root = Tk()
root.title("Normal Calculator")
root.geometry('1000x700')
root.configure(background='#a6d1d2')

entry_strvar = StringVar(root)

Label(root, text='NORMAL CALCULATOR', font=('Cambria', 30, "bold"),
      bg='lavender', fg='#535798', borderwidth=3, relief=RIDGE).place(x=310, y=40)

eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar,
                  width=25, font=('Arial', 20), state='disabled', borderwidth=3, relief=RIDGE)
eqn_entry.place(x=300, y=120)

digits = [
    ('7', 300, 200), ('8', 370, 200), ('9', 440, 200),
    ('4', 300, 270), ('5', 370, 270), ('6', 440, 270),
    ('1', 300, 340), ('2', 370, 340), ('3', 440, 340),
    ('0', 300, 410), ('.', 370, 410), ('%', 440, 410)
]
for (txt, x, y) in digits:
    Button(root, text=txt, height=2, width=5, font=('Arial', 12), bg='white',
           command=lambda t=txt: add_text(t, entry_strvar)).place(x=x, y=y)

operators = [
    ('/', 510, 200), ('*', 510, 270), ('-', 510, 340),
    ('+', 510, 410), ('(', 580, 200), (')', 580, 270)
]
for (txt, x, y) in operators:
    Button(root, text=txt, height=2, width=5, font=('Arial', 12), bg='lightsteelblue3',
           command=lambda t=txt: add_text(t, entry_strvar)).place(x=x, y=y)

Button(root, text='π', height=2, width=5, font=('Arial', 12), bg='lightsteelblue3',
       command=lambda: add_text(str(math.pi), entry_strvar)).place(x=580, y=340)

Button(root, text='C', height=2, width=5, font=('Arial', 12), bg='#205b7a', fg='white',
       command=lambda: entry_strvar.set(entry_strvar.get()[:-1])).place(x=580, y=410)

Button(root, text='AC', bg='#ff595e', fg='white',
       font=('Arial', 12, 'bold'), width=10,
       command=lambda: entry_strvar.set('')).place(x=300, y=480)

Button(root, text='=', bg='#1982c4', fg='white',
       font=('Arial', 12, 'bold'), width=10,
       command=lambda: submit(eqn_entry, entry_strvar)).place(x=430, y=480)

Button(root, text='EXIT', bg='#6a4c93', fg='white',
       font=('Arial', 12, 'bold'), width=10,
       command=root.destroy).place(x=560, y=480)

root.mainloop()
