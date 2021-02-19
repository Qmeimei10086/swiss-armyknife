from tkinter import*
import zipfile
import threading
from tkinter import messagebox
import io

global i
i = 0
bools = 1
def extractfile(zfile, password):
    try:
        zfile.extractall(pwd = password)
        print("[*]文件解压密码为: ", password)
        banner = '破解成功,密码: ' + password
        messagebox.showinfo("密码破解-zip",banner)
        return True
    except FileNotFoundError:
        print('路径错误')
    except:
        global i
        i = i + 1
        print("[-]密码尝试第%s次" % i + ':'+ password)
        return False
    else:
        print("[*]文件解压密码为: ", password)
        banner = '破解成功,密码: ' + password
        messagebox.showinfo("密码破解-zip",banner)
        return True
def main_zip(fale,number):
    print('[*]您选择了zip密码破解')
    messagebox.showinfo("密码破解-linux","破解开始")
    zfile = zipfile.ZipFile(fale)
    password_list = open('pwd.txt').read().splitlines()
    for Password in password_list:
        if bools:
            pwd = extractfile(zipfile,Password)
            if pwd:
                print('密码正确: '+ Password)


def start_password():
    global bools
    fale = en.get()
    bools = True
    number = 1
    t = threading.Thread(target=main_zip,args=(fale,number))
    t.start()
def stop_password():
    global bools
    bools = False
    messagebox.showinfo("密码破解-zip","破解结束")
    return True





#---------------------------------------------------
tk = Tk()
tk.title('密码破解-zip')
tk.geometry('300x160+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=80,y=40)
#--------------------------text------------------
w= Label(tk,text='目标文件:',fg="red")
w.place(x=20,y=40)
w2= Label(tk,text=' 注:请进行转意,例如 C:/user/a.zip --> C://user/a.zip',fg="red")
w2.place(x=0,y=120)
#------------------------start or stop----------------
b = Button(tk, text ="开始破解",command=start_password)
b.place(x=20,y=80)
b_2 = Button(tk, text ="停止",command=stop_password)
b_2.place(x=200,y=80)
tk.mainloop()
#------------------------start-GUI--------------------
tk.mainloop()
#-------------------------over-------------------------
#zfile.extractall(pwd = bytes(password, "utf8" ))
            #t = threading.Thread(target=extractfile, args=(zfile, Password))
            #t.start()
            #t.join()