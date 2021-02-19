import flask,json
from flask import request
import os
import threading
print('[+]在8888端口开启服务,请勿使用此端口')
def gui():
    os.system('GUI')





def arp():
    os.system(r'cmd /c python bin\attack\arp.py')

def arpspoof():
    os.system(r'cmd /c python bin\attack\arpspoof.py')

def dos():
    os.system(r'cmd /c python bin\dos\dos.py')

def passwd_win():
    os.system(r'cmd /c python bin\password\windows.py')

def ssh():
    os.system(r'cmd /c python bin\password\ssh.py')

def zip():
    os.system(r'cmd /c python bin\password\zip.py')

def listen_py():
    os.system(r'cmd /c python bin\listen\listen-python.py')

def listen_win():
    os.system(r'cmd /c python bin\listen\listen-windows.py')

def listen_powershell():
    os.system(r'cmd /c python bin\listen\listen-powershell.py')


def download():
    os.system(r'cmd /c python Download\Download.py')
def powershell():
    os.system(r'cmd /c python bin\summon\powershell.py')

def windows():
    os.system(r'cmd /c python bin\summon\windows.py')

def python():
    os.system(r'cmd /c python bin\summon\python.py')


def find_ip():
    os.system(r'cmd /c python bin\scanner\scanner.py')

def scan_port():
    os.system(r'cmd /c python bin\scanner\scanner-port.py')


def clone():
	os.system(r'cmd /c python bin\web\clone.py')

def php():
    os.system(r'cmd /c python bin\web\php.py')


def php_shell():
    os.system(r'cmd /c python bin\web\shell.py')


def l_win(lport):
	cmd = 'cmd /c python bin\listen\listen-py.py ' + lport
	os.system(cmd)

def scan():
	os.system(r'python scanner\scanner.py')



server = flask.Flask(__name__)
@server.route('/',methods=['get','post'])
def get():
    #获取通过url请求传参的数据
    cmd = request.values.get('cmd')
    #----------------------------
    if cmd:
        if cmd == 'arp':
            t = threading.Thread(target=arp)
            t.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        if cmd == 'arpspoof':
            t1 = threading.Thread(target=arpspoof)
            t1.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        #-----------------------------
        if cmd == 'dos':
            t2 = threading.Thread(target=dos)
            t2.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        #---------------------------
        if cmd == 'passwd-win':
            t3 = threading.Thread(target=passwd_win)
            t3.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        if cmd == 'ssh':
            t4 = threading.Thread(target=ssh)
            t4.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        if cmd == 'zip':
            t5 = threading.Thread(target=zip)
            t5.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        #---------------------------
        if cmd == 'listen-py':
            t6 = threading.Thread(target=listen_py)
            t6.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        if cmd == 'listen-win':
            listen_win()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        if cmd == 'listen_powershell':
            listen_powershell()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)



        #-------------------------
        if cmd == 'powershell':
            
            t7 = threading.Thread(target=download)
            t7.start()
            t8 = threading.Thread(target=powershell)
            t8.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)

        if cmd == 'windows':
            t9 = threading.Thread(target=windows)
            t9.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)

        if cmd == 'python':
            t10 = threading.Thread(target=python)
            t10.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)

        #------------------------

        if cmd == 'find-ip':
            t11 = threading.Thread(target=find_ip)
            t11.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        
        if cmd == 'scan-port':
            t12 = threading.Thread(target=scan_port)
            t12.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)

        #----------------------
        if cmd == 'clone':
            t13 = threading.Thread(target=clone)
            t13.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)
        if cmd == 'web-php':
            t14 = threading.Thread(target=php)
            t14.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)


        if cmd == 'php-shell':
            t15 = threading.Thread(target=php_shell)
            t15.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)

        #-----------------------
        if cmd == 'scanner':
            t16 = threading.Thread(target=scan)
            t16.start()
            resu={'code':200,'message':'ok'}
            return json.dumps(resu,ensure_ascii=False)



if __name__== '__main__':
    print('[*]service is start on 127.0.0.1:8888')
    t17 = threading.Thread(target=gui)
    t17.start()
    server.run(port = 8888,host='0.0.0.0')
