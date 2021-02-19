import socket
import time
from threading import Thread
from tkinter import*
from tkinter import messagebox
ip_list = []
def main(ip):
    f = open('port.txt','w')
    print("开始扫描:%s"%ip)
    #扫描1~1024端口
    for port in range(1,10000):
        #创建多线程扫描,target参数是多线程执行的方法，args参数是方法所需参数
        t = Thread(target=portScan, args=(ip, port))
        #启动多线程
        t.start()
    ban = '以下端口可能开放: \n'
    for ip in ip_list:
        ban += str(ip) + '\n'
        f.write(str(ip)+'\n')
        
    messagebox.showinfo("scanner",ban)
    f.close()
#定义portScan涵数，用来进行TCP端口扫描
def portScan(ip, port=443):
    try:
        #创建socket链接
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #尝试链接
        client.connect((ip, port))
        print("[*] %s:%d 开放"%(ip, port) + '\n')
        ip_list.append(port)


    except:
        #连接失败时会抛出异常，导致程序不会继续执行，所以这里要捕获
        pass
 


def start():
        ip = en.get()
        main(ip)
def stop():
        pass

#---------------------------------------------------
tk = Tk()
tk.title('端口扫描')
tk.geometry('300x160+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=80,y=40)
#--------------------------text------------------
w= Label(tk,text='目标IP:',fg="red")
w.place(x=20,y=40)
#------------------------start or stop----------------
b = Button(tk, text ="开始扫描", command=start)
b.place(x=20,y=80)
b_2 = Button(tk, text ="停止", command=stop)
b_2.place(x=200,y=80)
tk.mainloop()
#------------------------start-GUI--------------------
tk.mainloop()
#-------------------------over-------------------------

