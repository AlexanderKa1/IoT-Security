
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
import datagram
import objects

p = rfid.rfid()#RFID init

server = ('2607:f2c0:e344:a01::6665',7000)
bind_addr = ('2607:f2c0:e344:a02::2:2',7000)
what = {'scan':1001}

#network init
#-----------------------------------------------------------------#
os.system('ip -6 addr add 2607:f2c0:e344:a02::2:2/64 dev wlan0')
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(bind_addr)
s.connect(server)
#-----------------------------------------------------------------#
def callback(uid):
    global s,p
    part = uid[0].to_bytes(1,'little')+uid[1].to_bytes(1,'little')+uid[2].to_bytes(1,'little')+uid[3].to_bytes(1,'little')+uid[4].to_bytes(1,'little')
    addr = b'\x26\x07\xf2\xc0\xe3\x44\x0a\x03\x00\x01\x00'+part
    ipv6 = ipaddress.IPv6Address(addr)
    if p.db[uid] == 'Error':
        print('Error Read!')
        return
    else:
        print('Scan:',str(ipv6))
        g = datagram.dict_datagram()
        g['what_how'] = objects.what['scan']
        g['when'] = time.time()
        s.send(g.encode())

while True:
    p.thread(callback)
