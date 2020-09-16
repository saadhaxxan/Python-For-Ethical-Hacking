#!/usr/bin/python

import socket
from termcolor import colored


print(colored("Select Option"),"blue")
print(colored("1. Single Port\n2. Multi Port"),"blue")
option = int(input())

if option == 1:
    print(colored("Enter Host IP Address:","green"))
    host = input()
    print(colored("Enter port number to scan:","green"))
    port = int(input())

if option == 2:
    print(colored("[*] Enter Host IP Address:","green"))
    host = input()
    print(colored("[*] Enter number of ports to scan:","green"))
    num = int(input())

def getBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        soc = socket.socket()
        soc.connect((ip, port))
        banner = soc.recv(1024)
        return banner 
    except:
        return "Got Nothing"

def PScanner(host,port,option):
    if option == 1:
        banner = getBanner(host, port)
        if banner:
            print(colored("[+]" + host + '/' + str(port) + ":" + banner.strip('\n'),"blue"))
    if option == 2:
        for port in range(1,num):
            banner = getBanner(host, port)
            print(colored("[+] " + host + '/' + str(port) + ": " + banner.strip('\n'),"blue"))

if option == 1:
    PScanner(host,port,option)

if option == 2:
    PScanner(host,num,option)