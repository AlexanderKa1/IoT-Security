
#-----------------------------------------------------------------#
#                               Ark Sun                           #
#                             2018-10-20                          #
#                        arksun9481@gmail.com                     #
#-----------------------------------------------------------------#

import bsp
import time
import threading
import os
import socket
import ipaddress
import struct

server_addr = ('2607:f2c0:e344:a01::6665',7000)
bind_addr = ('2607:f2c0:e344:a02::3:2',7000)
what = {'click':1}

#network init
#-----------------------------------------------------------------#
os.system('ip -6 addr add 2607:f2c0:e344:a02::3:2/64 dev wlan0')
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(bind_addr)
s.connect(server_addr)
#-----------------------------------------------------------------#
def callback(addr):
    global s
    t = time.time()
    ipv6 = str(ipaddress.IPv6Address(addr))
    print('click:',ipv6)
    s.send(str([1,time.time(),bind_addr[0],ipv6,None]).encode())

bsp.buttons_mo[0].register(callback)
bsp.buttons_mo[1].register(callback)
bsp.buttons_mo[2].register(callback)
bsp.buttons_mo[3].register(callback)

while True:
    cmd = input("buttons>")
    if cmd == 'exit':
        break
