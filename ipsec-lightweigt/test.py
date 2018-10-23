import ctypes
import os
import socket

os.system('gcc -shared -fPIC ipsec.c aes.c')

l = ctypes.cdll.LoadLibrary('./a.out')
a = l.isakmp_len()
l.isakmp.restype = ctypes.POINTER(ctypes.c_ubyte)
b = l.isakmp()
data = b''.join([b[i].to_bytes(1,'big') for i in range(a)])

s = socket.socket(socket.AF_INET6,socket.SOCK_RAW,socket.IPPROTO_ESP)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('::',0))
s.connect(('2607:F2C0:E344:A02:260A:C4FF:FE0F:C338',0))
s.send(data)

