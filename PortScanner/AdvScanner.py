#!/usr/bin/python


from socket import *
import socket
from termcolor import colored
from threading import *


print(colored("[*] Enter Host IP Address or Website Name:","green"))
host = input()
print(colored("[*] Enter number of ports to scan:","green"))
num = int(input())

def PScanner(port):    
    # AF_INT means we want to connect to IPv4 and IPv6 Addresses
    # SOCK_STREAM means we want to connect using the TCP protocol not the UDP
    try:
        soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        soc.connect((host,port))
        print(colored("[+] %d/tcp is Open" %(port),"blue"))
    
    except:
        print(colored("[!!] %d/tcp is Closed" %(port),"red"))
    finally:
        soc.close()

def ResolveScan(tHost,tPorts):
    try:
        targetIP = gethostbyname(tHost)
    except:
        print(colored("Unknown Host"),"red")
    try:
        targetname = gethostbyaddr(targetIP)
        print(colored("[+] Scan results for: "+ targetname[0],"blue"))
    except:
        print(colored("[+] Scan Results for: "+ targetIP,"blue"))
    
    setdefaulttimeout(1)

    for port in range(1,num):
        PScanner(port)


ResolveScan(host,num)