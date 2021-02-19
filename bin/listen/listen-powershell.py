from tkinter import*
from tkinter import messagebox
import os




def start():
    lport = en.get()
    os.system('cd nc && nc -lvp '+lport)
    os.system('dir')

def stop():
	pass

#---------------------------------------------------
tk = Tk()
tk.title('监听-powershell')
tk.geometry('300x160+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=80,y=40)
#--------------------------text------------------
w= Label(tk,text='端口:',fg="red")
w.place(x=20,y=40)
#------------------------start or stop----------------
b = Button(tk, text ="开始监听", command=start)
b.place(x=20,y=80)
b_2 = Button(tk, text ="停止", command=stop)
b_2.place(x=200,y=80)
tk.mainloop()