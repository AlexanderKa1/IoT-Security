
#-----------------------------------------------------------------#
#                               Ark Sun                           #
#                             2018-10-18                          #
#                        arksun9481@gmail.com                     #
#-----------------------------------------------------------------#

import bsp
import time
import rfid
import threading
import os
import socket
import ipaddress

p = rfid.rfid()#RFID init

server = ('2607:f2c0:e344:a02::2:3',7000)

#network init
#-----------------------------------------------------------------#
os.system('ip -6 addr add 2607:f2c0:e344:a02::2:2/64 dev wlan0')
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('2607:f2c0:e344:a02::2:2',7000))
s.connect(server)
s.connect(server)
#-----------------------------------------------------------------#
def callback(uid):
    global s,p
    part = uid[0].to_bytes(1,'little')+uid[1].to_bytes(1,'little')+uid[2].to_bytes(1,'little')+uid[3].to_bytes(1,'little')+uid[4].to_bytes(1,'little')
    addr = b'\x26\x07\xf2\xc0\xe3\x44\x0a\x03\x00\x01\x00'+part
    if uid not in p.db:
        print('Other:',addr)
        return
    if p.db[uid] == 'Alice':
        print('Alice',addr)
        s.send(str(ipaddress.IPv6Address(addr)).encode())
        return
    if p.db[uid] == 'Bob':
        print('Bob',addr)
        s.send(str(ipaddress.IPv6Address(addr)).encode())
        return
    print(p.db[uid],addr)

while True:
    p.thread(callback)
