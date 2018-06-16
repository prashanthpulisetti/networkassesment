from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from tkinter import *
import subprocess
from textwrap import wrap
from tkinter import BOTH, END, LEFT
from PyPDF2 import PdfFileMerger

def lets_scan():
   e2.delete("1.0",END)
   cmd =("ip route show | grep 'default' | awk '{print $3}' ") 
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   line = proc.stdout.readline()
   e1.insert(END,line)
   ip=line[:-1]
   cmd =("nmap -sP %s/24" %(ip))  
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   c = canvas.Canvas('Report.pdf')
   c.drawString( 10,800, "")
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
   
   

   cmd =("ip route show | grep 'default' | awk '{print $3}' ") 
   pro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   line = proc.stdout.readline()
   e1.insert(END,line)
   ip=line[:-1]
   cmd =("timeout 30 nmap -sS -sU -A -v")+ ip  
   pro = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   #c = canvas.Canvas('2.pdf')
   c.drawString( 10,800, "")
   i = 0
   while True:
     line = pro.stdout.readline()
     c.drawString(10,800 - i,line[:-1])
     i = i + 15
     if not line:
         break
     e2.insert(END,line)
     
     e2.update_idletasks()
   e2.insert(END,"\n\n..........exit")
   c.showPage()
   

   #url=e1.get("1.0",END)
   cmd =("arp-scan --interface=wlan0 --localnet")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("arp-scan --interface=wlan0 --localnet") 
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   #c = canvas.Canvas('3.pdf')
   #c.drawString( 10,750, "3.Arp-scan Tool")
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
  

   e2.delete("1.0",END)
   cmd =("ip route show | grep 'default' | awk '{print $3}' ")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   line = proc.stdout.readline()
   e1.insert(END,line)
   ip=line[:-1]
   cmd=("doona -m HTTP -t ") + ip + (" -M 20" )
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   #c = canvas.Canvas('ex.pdf')
   #c.drawString( 10,750, "4.Doona Tool")
   i=0
   while True:
	line = proc.stdout.readline()
  	c.drawString(10,800 -i,line[:-1])
	i = i + 15
	if not line:
	    break
	e2.insert(END,line)

	e2.update_idletasks()
   e2.insert(END,"\n\n...............exit")
	

   c.showPage()
   
   e2.delete("1.0",END)
   cmd =("ip route show | grep 'default' | awk '{print $3}' ") 
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   line = proc.stdout.readline()
   e1.insert(END,line)
   ip=line[:-1]
   cmd =("oscanner -s %s/24" %(ip))  
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   #c = canvas.Canvas('oscanner.pdf')
   c.drawString( 10,750, "")
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


   e2.delete("1.0",END)
   cmd =("ip route show | grep 'default' | awk '{print $3}' ")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   line = proc.stdout.readline()
   e1.insert(END,line)
   ip=line[:-1]
   cmd=("smtp-user-enum -M VRFY -u root -t ") + ip
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   #c = canvas.Canvas('smpt-user-enum.pdf')
   i=0
   while True:
	line = proc.stdout.readline()
  	c.drawString(10,800 -i,line[:-1])
	i = i + 15
	if not line:
	    break
	e2.insert(END,line)

	e2.update_idletasks()
   e2.insert(END,"\n\n...............exit")
   c.showPage()

   cmd =("timeout 8 bettercap -X")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   cmd =("timeout 8 bettercap -X")
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   #c = canvas.Canvas('bettercap.pdf')
   t = c.beginText()
   t.setFont('Helvetica', 10,)
   t.setCharSpace(1.2)
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
master = Tk()
master.title("information scanner")
Label(master, text="Ip").grid(row=0)
Label(master, text="Output").grid(row=2)

e1 = Text(master,height=1, width=100)
e2 = Text(master,height=20, width=100)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=6, sticky=W, pady=4)
Button(master, text='Scan', command=lets_scan).grid(row=3, column=7, sticky=W, pady=4)

mainloop( )
