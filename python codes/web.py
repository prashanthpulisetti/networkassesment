#for Python 2
import Tkinter as tk
import ttk
from tkinter import BOTH, END, LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import os,sys
#for Python 3
#import tkinter as tk
#from tkinter import ttk
import subprocess
 
import platform

def sql():
   
   e2.delete("1.0",END)
   url=e1.get("1.0",END)
   cmd =("sqlmap -u") + url + ("--dbs")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("sqlmap -u") + url + ("--dbs")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('sqlmap.pdf')
   i = 0
   while True:
     
     line = proc.stdout.readline()
     c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     e2.insert(END,line)
     
     e2.update_idletasks()
   e2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()

def commix():
   f2.delete("1.0",END)
   url=f1.get("1.0",END)
   cmd =("commix -u") + url + ("--all")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("commix -u") + url + ("--all")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('com.pdf')
   i = 0
   while True:
     line = proc.stdout.readline()
     c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     f2.insert(END,line)
     
     f2.update_idletasks()
   f2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()
 
def fimap():
   g2.delete("1.0",END)
   url=g1.get("1.0",END)
   cmd =("fimap -u") + url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("fimap -u") + url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('fi.pdf')
   i = 0
   while True:
     line = proc.stdout.readline()
     c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     g2.insert(END,line)
     
     g2.update_idletasks()
   g2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()

def hurl():
   h2.delete("1.0",END)
   url=h1.get("1.0",END)
   cmd =("hURL -b") + url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("hURL -b") + url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('hurl.pdf')
   i = 0
   while True:
     line = proc.stdout.readline()
     c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     h2.insert(END,line)
     
     h2.update_idletasks()
   h2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()

def grab():
   i2.delete("1.0",END)
   url=i1.get("1.0",END)
   cmd =("grabber --spider 1 --sql --xss --url ") + url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("grabber --spider 1 --sql --xss --url ") + url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('grabb.pdf')
   i = 0
   while True:
     line = proc.stdout.readline()
     c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     i2.insert(END,line)
     
     i2.update_idletasks()
   i2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()
def home():
    
    os.system("python xxx.py")

def quit():
    global tkTop
    tkTop.destroy()
 
tkTop = tk.Tk()
tkTop.geometry('500x500')
 

 
notebook = ttk.Notebook(tkTop)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
notebook.add(frame1, text='SQL MAP')
notebook.add(frame2, text='COMMIX')
notebook.add(frame3, text='FIMAP')
notebook.add(frame4, text='HURL')
notebook.add(frame5, text='GRABBER')
notebook.pack()
 
tkButtonQuit = tk.Button(
    tkTop,
    text="Quit",
    command=quit)
tkButtonQuit.pack()

e1 = tk.Text(frame1,height=1, width=50)
e1.pack()

f1 = tk.Text(frame2,height=1, width=50)
f1.pack()

g1 = tk.Text(frame3,height=1, width=50)
g1.pack()

h1 = tk.Text(frame4,height=1, width=50)
h1.pack()

i1 = tk.Text(frame5,height=1, width=50)
i1.pack()

e2 = tk.Text(frame1,height=20, width=100)
e2.pack()

f2 = tk.Text(frame2,height=20, width=100)
f2.pack()

g2 = tk.Text(frame3,height=20, width=100)
g2.pack()

h2 = tk.Text(frame4,height=20, width=100)
h2.pack()

i2 = tk.Text(frame5,height=20, width=100)
i2.pack()
  
b1 = tk.Button(
    frame1,
    text="Scan",command=sql)
b1.pack()
b2 = tk.Button(
    frame2,
    text="Scan",command=commix)
b2.pack()
b3 = tk.Button(
    frame3,
    text="Scan",command=fimap)
b3.pack()
b4 = tk.Button(
    frame4,
    text="Scan",command=hurl)
b4.pack()
b5 = tk.Button(
    frame5,
    text="Scan",command=grab)
b5.pack()
b6 = tk.Button(
    frame5,
    text="home",command=home)
b6.pack()
b7 = tk.Button(
    frame4,
    text="home",command=home)
b7.pack()
b8 = tk.Button(
    frame3,
    text="home",command=home)
b8.pack()
b9 = tk.Button(
    frame2,
    text="home",command=home)
b9.pack()
b10 = tk.Button(
    frame1,
    text="home",command=home)
b10.pack()

tkTop.title("web analsys")
   

 

 
tk.mainloop()
