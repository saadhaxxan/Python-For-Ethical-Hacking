#! /usr/bin/python

from scapy.all import *

def findDns(p):
    if p.haslayer(DNS):
        print(p[IP].src)
        print(p[DNS].summary())

sniff(prn=findDns)