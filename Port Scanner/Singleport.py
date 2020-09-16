#!/usr/bin/python

import socket
from termcolor import colored

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# AF_INT means we want to connect to IPv4 and IPv6 Addresses
# SOCK_STREAM means we want to connect using the TCP protocol not the UDP

print(colored("Enter Host IP Address:","green"))
host = input()
print(colored("Enter port number to scan:","green"))
port = int(input())

def PScanner(host,port):
    if soc.connect_ex((host,port)):
        print(colored("PORT %d is closed" %(port),"red"))
    
    else:
        print(colored("PORT %d is open" %(port),"blue"))

PScanner(host,port)