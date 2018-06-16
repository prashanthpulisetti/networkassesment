

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from tkinter import *
import subprocess

def lets_scan():
   e2.delete("1.0",END)
   cmd =("ip route show | grep 'default' | awk '{print $3}' ") 
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   line = proc.stdout.readline()
   e1.insert(END,line)
   ip=line[:-1]
   cmd =("nmap -sP %s/24" %(ip))  
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('single.pdf')
   i = 0
   while True:
     line = proc.stdout.readline()
     c.drawString(50,500 - i,line[:-1])
     i = i + 15
     if not line:
         break
     e2.insert(END,line)
     
     e2.update_idletasks()
   e2.insert(END,"\n\n..........exit")
   

   cmd =("ip route show | grep 'default' | awk '{print $3}' ") 
   pro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   line = proc.stdout.readline()
   e1.insert(END,line)
   ip=line[:-1]
   cmd =("nmap -T4 -A -v")+ ip  
   pro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   #c = canvas.Canvas('single.pdf')
   i = 0
   while True:
     line = pro.stdout.readline()
     c.drawString(50,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     e2.insert(END,line)
     
     e2.update_idletasks()
   e2.insert(END,"\n\n..........exit")
 
   c.showPage()
   c.save()

master = Tk()
master.title("SIngle")
Label(master, text="Ip").grid(row=0)
Label(master, text="Output").grid(row=2)

e1 = Text(master,height=1, width=100)
e2 = Text(master,height=20, width=100)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=6, sticky=W, pady=4)
Button(master, text='Scan', command=lets_scan).grid(row=3, column=7, sticky=W, pady=4)

mainloop( )
