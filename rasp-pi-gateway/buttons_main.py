#!/usr/bin/python3
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
import datagram
import objects
import ipaddress
#****************************************************#
server_addr = ('2607:f2c0:e344:a01::6665',7000)
bind_addr = ('2607:f2c0:e344:a02::3:2',7000)
#****************************************************#
#network init
#-----------------------------------------------------------------#
output = os.popen('ip -6 addr add 2607:f2c0:e344:a02::3:2/64 dev wlan0')
time.sleep(3)
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(bind_addr)
s.connect(server_addr)
s.settimeout(0.5)
#-----------------------------------------------------------------#
flag = True

def callback(addr):
    global s
    print('click:',ipaddress.IPv6Address(addr))
    g = datagram.dict_datagram()
    g['what_how'] = objects.what['push']
    g['when'] = time.time()
    g['where'] = ipaddress.IPv6Address(objects.objects['gateway_buttons'])
    g['which_who'] = ipaddress.IPv6Address(addr)
    try:
        s.send(g.encode())
    except ConnectionRefusedError:
        print('lose connection')
    

bsp.buttons_mo[0].register(callback)
bsp.buttons_mo[1].register(callback)
bsp.buttons_mo[2].register(callback)
bsp.buttons_mo[3].register(callback)

if __name__=='__main__':
    while flag:
        cmd = input("buttons>")
        if cmd == 'exit':
            flag = False



