from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from tkinter import *
import subprocess
import time
def lets_scan():
   e2.delete("1.0",END)
   url=e1.get("1.0",END)
   cmd =("netdiscover -r ") + url
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("netdiscover -r ") + url 
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('arp.pdf')
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
   time.sleep(1)

master = Tk()
master.title("arpscan")
Label(master, text="arpscan").grid(row=0)
Label(master, text="Output").grid(row=1)

e1 = Text(master,height=1, width=100)
e2 = Text(master,height=30, width=100)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=6, sticky=W, pady=4)
Button(master, text='Scan', command=lets_scan).grid(row=3, column=7, sticky=W, pady=4)

mainloop( )
