from tkinter import *
import subprocess
import time

def lets_scan():
   e2.delete("1.0",END)
   ip=e1.get("1.0",END)
   cmd =("netdiscover -r") + ip
   proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
   
   while True:
     line = proc.stdout.readline()
     if not line:
         break
     e2.insert(END,line)
     
     e2.update_idletasks()
   e2.insert(END,"\n\n..........exit")

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False
master = Tk()
master.title("Netdiscover")
Label(master, text="enter ip range").grid(row=0)
Label(master, text="Output").grid(row=1)

e1 = Text(master,height=1, width=100)
e2 = Text(master,height=20, width=100)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
stop = Button(master, text="Stop", command=stop)
stop.grid()
Button(master, text='Quit', command=master.quit).grid(row=3, column=6, sticky=W, pady=4)
Button(master, text='Scan', command=lets_scan).grid(row=3, column=7, sticky=W, pady=4)

mainloop( )
