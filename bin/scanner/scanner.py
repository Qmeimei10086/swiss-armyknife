from scapy.all import *
from tkinter import messagebox

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        lhost=s.getsockname()[0]
    finally:
        s.close()

    return lhost


def worker(lhost):
    host = lhost[:10]
    ip_list=[]
    for ipFix in range(1,20):
        ip= host +str(ipFix)
        arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
        res = srp1(arpPkt, timeout=1, verbose=False)
        if res:
            print ("IP: " + res.psrc + "     MAC: " + res.hwsrc)
            ip_list.append(res.psrc)
    return ip_list
if __name__=="__main__":
    lhost = get_host_ip()
    
    fp = open('ip.txt','w')
    ip_list = worker(lhost)
    i = 0
    for ip in ip_list:
        fp.write(ip+'\n')
        i += 1
    print("扫描到的IP数:"+str(i))
    ip_scanner = '以下主机可能存活: \n'
    for ip in ip_list:
        #ip_scanner = '以下主机可能存活: \n'
        ip_scanner += ip + '\n'


    messagebox.showinfo("scanner",ip_scanner)
    fp.close()


