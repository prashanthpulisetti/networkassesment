import os,sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from tkinter import *
import subprocess

def web():
   os.system("python web.py")

def vulna():
   os.system("python information.py")
   
master = Tk()
master.title("NETWORK ASSESMENT")
Label(master, text="NETWORK ASSESMENT")
master.geometry('400x200')
Label(master, text="WEB analysis").grid(row=1,column=1)
Label(master, text="Vulnerable scanner").grid(row=3,column=1)

Button(master, text='vulnerable scanner', command=vulna).grid(rows=1, column=2, sticky=W, pady=4)
Button(master, text='web analysis', command=web).grid(row=2, column=2, sticky=W, pady=4)

Button(master, text='Quit', command=master.quit).grid(rows=10, column=6, sticky=W, pady=4)


mainloop()
