# !usr/bin/python

import hashlib
from termcolor import colored

print(colored("[*] Enter string or password to hash","blue"))
hashval = str(input())

print(colored("[*] Enter the hash you want to do",'blue'))
print(colored("1. MD5\n2. SHA1\n3. SHA224\n4. SHA256\n5. SHA512\n6. All",'green'))
option = int(input())

if option == 1:
    md5obj = hashlib.md5()
    md5obj.update(hashval.encode())
    print(colored("Your hash is: "+ md5obj.hexdigest(),'green'))

if option == 2:
    sha1obj = hashlib.sha1()
    sha1obj.update(hashval.encode())
    print(colored("Your hash is: "+ sha1obj.hexdigest(),'green'))

if option == 3:
    sha224obj = hashlib.sha224()
    sha224obj.update(hashval.encode())
    print(colored("Your hash is: "+ sha224obj.hexdigest(),'green'))

if option == 4:
    sha256obj = hashlib.sha256()
    sha256obj.update(hashval.encode())
    print(colored("Your hash is: "+ sha256obj.hexdigest(),'green'))

if option == 5:
    sha512obj = hashlib.sha512()
    sha512obj.update(hashval.encode())
    print(colored("Your hash is: "+ sha512obj.hexdigest(),'green'))

if option == 6:
    md5obj = hashlib.md5()
    md5obj.update(hashval.encode())
    print(colored("MD5 is: "+ md5obj.hexdigest(),'green'))
    sha1obj = hashlib.sha1()
    sha1obj.update(hashval.encode())
    print(colored("SH1 is: "+ sha1obj.hexdigest(),'green'))
    sha224obj = hashlib.sha224()
    sha224obj.update(hashval.encode())
    print(colored("SHA224 is: "+ sha224obj.hexdigest(),'green'))
    sha256obj = hashlib.sha256()
    sha256obj.update(hashval.encode())
    print(colored("SHA256 is: "+ sha256obj.hexdigest(),'green'))
    sha512obj = hashlib.sha512()
    sha512obj.update(hashval.encode())
    print(colored("SHA512 is: "+ sha512obj.hexdigest(),'green'))