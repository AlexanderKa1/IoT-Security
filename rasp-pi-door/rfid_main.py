
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

p = rfid.rfid()#RFID init

#network init
#-----------------------------------------------------------------#
os.system('ip -6 addr add 2607:f2c0:e344:a02::2:2/64 dev wlan0')
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('2607:f2c0:e344:a02::2:2',7000))
s.connect(('2607:f2c0:e344:a02::2:3',7000))
#-----------------------------------------------------------------#
def callback(uid):
    global s,p
    if uid not in p.db:
        print('Other:',uid)
        return
    if p.db[uid] == 'Alice':
        print('Alice',uid)
        s.send('Alice'.encode())
        return
    if p.db[uid] == 'Bob':
        print('Bob',uid)
        s.send('Bob'.encode())
        return
    print(p.db[uid],uid)

while True:
    p.thread(callback)
