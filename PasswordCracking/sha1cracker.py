# !usr/bin/python

import hashlib
from termcolor import colored
from urllib.request import urlopen

print(colored("[*] Enter SHA1 hashed value","blue"))
hashval = str(input())

#  We are using 1 million password dictionary to find our the SH1 hash reverse value
passwordlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(),'utf-8')

print(colored("Password matching started\n",'green'))
for password in passwordlist.split('\n'):
    hashguess = hashlib.sha1(bytes(password,'utf-8')).hexdigest()
    if hashguess == hashval:
        print(colored("Password found !! it is "+ str(password),'green'))
        quit()
    else:
        print(colored('dont matched trying next.....','red'))
    
print(colored("Password not in the list",'red'))