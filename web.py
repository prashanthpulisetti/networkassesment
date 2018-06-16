#for Python 2
import Tkinter as tk
import ttk
from tkinter import BOTH, END, LEFT
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from textwrap import wrap
import tkFont
import os,sys
#for Python 3
#import tkinter as tk
#from tkinter import ttk
import subprocess
 
import platform

def sql():
   
   e2.delete("1.0",END)
   url=e1.get("1.0",END)
   cmd =("sqlmap -u")+ url +("--dbs")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("sqlmap -u")+ url +("--dbs")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('sqlmap.pdf')
   t = c.beginText()
   t.setFont('Helvetica', 9)
   t.setCharSpace(1.5)
   t.setTextOrigin(50, 700)
   i = 0
   while True:
     line = proc.stdout.readline()
     w_line = "\n".join(wrap(line,80))
     t.textLines(w_line)
     c.drawText(t)
     #c.drawString(10,800 - i,line[:-1])
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
   t = c.beginText()
   t.setFont('Helvetica', 9)
   t.setCharSpace(1.5)
   t.setTextOrigin(50, 700)
   i = 0
   while True:
     line = proc.stdout.readline()
     w_line = "\n".join(wrap(line,10))
     t.textLines(w_line)
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
   t = c.beginText()
   t.setFont('Helvetica', 9)
   t.setCharSpace(1.5)
   t.setTextOrigin(50, 700)
   i = 0
   while True:
     line = proc.stdout.readline()
     w_line = "\n".join(wrap(line,80))
     t.textLines(w_line)
     c.drawText(t)
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
   t = c.beginText()
   t.setFont('Helvetica', 9)
   t.setCharSpace(1.5)
   t.setTextOrigin(50, 700)
   i = 0
   while True:
     line = proc.stdout.readline() 
     w_line = "\n".join(wrap(line,80))
     t.textLines(w_line)
     c.drawText(t)
     #c.drawString(10,800 - i,line[:-1])
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
   t = c.beginText()
   t.setFont('Helvetica', 9)
   t.setCharSpace(1.5)
   t.setTextOrigin(50, 700)
   i = 0
   while True:
     line = proc.stdout.readline()
     w_line = "\n".join(wrap(line,80))
     t.textLines(w_line)
     c.drawText(t)
     #c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     i2.insert(END,line)
     
     i2.update_idletasks()
   i2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()
def wpscan():
   j2.delete("1.0",END)
   url=j1.get("1.0",END)
   cmd =("wpscan --url ")+url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("wpscan --url ")+url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('wpscan.pdf')
   t = c.beginText()
   t.setFont('Helvetica', 7)
   t.setCharSpace(1.2)
   t.setTextOrigin(5,800)
   i = 0
   while True:
     line = proc.stdout.readline()
     w_line = "\n".join(wrap(line,80))
     t.textLines(w_line)
     c.drawText(t)
     #c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     j2.insert(END,line)
     
     j2.update_idletasks()
   j2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()
def lbd():
   k2.delete("1.0",END)
   url=k1.get("1.0",END)
   cmd =("lbd ")+url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("lbd ")+url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('lbd.pdf')
   t = c.beginText()
   t.setFont('Helvetica', 9)
   t.setCharSpace(1.5)
   t.setTextOrigin(50, 700)
   i = 0
   while True:
     line = proc.stdout.readline()
     w_line = "\n".join(wrap(line,80))
     t.textLines(w_line)
     c.drawText(t)
     #c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     k2.insert(END,line)
     
     k2.update_idletasks()
   k2.insert(END,"\n\n..........exit")
   c.showPage()
   c.save()
def home():
    
    os.system("python home.py")

def pdf1():
    os.system("xdg-open sqlmap.pdf")
def pdf2():
    os.system("xdg-open com.pdf")
def pdf3():
    os.system("xdg-open fi.pdf")
def pdf4():
    os.system("xdg-open hurl.pdf")
def pdf5():
    os.system("xdg-open grabb.pdf")
def pdf6():
    os.system("xdg-open wpscan.pdf")
def pdf7():
    os.system("xdg-open lbd.pdf")


def quit():
    global tkTop
    tkTop.destroy()
 
tkTop = tk.Tk()
tkTop.geometry('1000x500')
 
notebook = ttk.Notebook(tkTop)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
frame6 = ttk.Frame(notebook)
frame7 = ttk.Frame(notebook)
notebook.add(frame1, text='SQL MAP')
notebook.add(frame2, text='COMMIX')
notebook.add(frame3, text='FIMAP')
notebook.add(frame4, text='HURL')
notebook.add(frame5, text='GRABBER')
notebook.add(frame6, text='WPSCAN')
notebook.add(frame7, text='LBD')
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

j1 = tk.Text(frame6,height=1, width=50)
j1.pack()

k1 = tk.Text(frame7,height=1, width=50)
k1.pack()

e2 = tk.Text(frame1,height=20, width=500)
e2.pack()

f2 = tk.Text(frame2,height=20, width=500)
f2.pack()

g2 = tk.Text(frame3,height=20, width=500)
g2.pack()

h2 = tk.Text(frame4,height=20, width=500)
h2.pack()

i2 = tk.Text(frame5,height=20, width=500)
i2.pack()

j2 = tk.Text(frame6,height=20, width=500)
j2.pack()

k2 = tk.Text(frame7,height=20, width=500)
k2.pack()

  
b1 = tk.Button(frame1,text="Scan",command=sql)
b1.pack()
b2 = tk.Button(frame2,text="Scan",command=commix)
b2.pack()
b3 = tk.Button(frame3,text="Scan",command=fimap)
b3.pack()
b4 = tk.Button(frame4,text="Scan",command=hurl)
b4.pack()
b5 = tk.Button(frame5,text="Scan",command=grab)
b5.pack()
b6 = tk.Button(frame5,text="home",command=home)
b6.pack()
w1 = tk.Button(frame6,text="scan",command=wpscan)
w1.pack()
lb1 = tk.Button(frame7,text="scan",command=lbd)
lb1.pack()
lb2 = tk.Button(frame7,text="home",command=home)
lb2.pack()
w2 = tk.Button(frame6,text="home",command=home)
w2.pack()
b7 = tk.Button(frame4,text="home",command=home)
b7.pack()
b8 = tk.Button(frame3,text="home",command=home)
b8.pack()
b9 = tk.Button(frame2,text="home",command=home)
b9.pack()
b10 = tk.Button(frame1,text="home",command=home)
b10.pack()
lb = tk.Button(frame7,text="Open PDF",command=pdf7)
lb.pack()
wp = tk.Button(frame6,text="Open PDF",command=pdf6)
wp.pack()
p6 = tk.Button(frame5,text="Open PDF",command=pdf5)
p6.pack()
p7 = tk.Button(frame4,text="Open PDF",command=pdf4)
p7.pack()
p8 = tk.Button(frame3,text="Open PDF",command=pdf3)
p8.pack()
p9 = tk.Button(frame2,text="Open PDF",command=pdf2)
p9.pack()
p10 = tk.Button(frame1,text="Open PDF",command=pdf1)
p10.pack()
tkTop.title("web analsys")
  

tk.mainloop()
