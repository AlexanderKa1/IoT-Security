#!/usr/bin/python3
#-----------------------------------------------------------------#
#                               Ark Sun                           #
#                             2018-10-23                          #
#                        arksun9481@gmail.com                     #
#-----------------------------------------------------------------#
import bsp
import time
import threading
import os
import socket
import datagram
import objects
#****************************************************#
server_addr = ('2607:f2c0:e344:a01::6665',7000)
bind_addr = ('2607:f2c0:e344:a02::2:3',7000)
#****************************************************#
#network init
#-----------------------------------------------------------------------
output = os.popen('ip -6 addr add 2607:f2c0:e344:a02::2:3/64 dev wlan0')
time.sleep(3)
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(bind_addr)
s.connect(server_addr)
s.settimeout(0.5)
#-----------------------------------------------------------------------

def nothing(append=None):
    pass
def unlock(append=None):
    click(bsp.sw_module)
def on(append=None):
    bsp.sw_module[0].on()
    bsp.sw_module[1].on()
def off(append=None):
    bsp.sw_module[0].off()
    bsp.sw_module[1].off()
def click(x):
    x[0].on()
    x[1].on()
    time.sleep(0.2)
    x[0].off()
    x[1].off()

flag = True

def net_main():
    global flag,s
    while True:
        try:
            data = s.recv(1000)
        except socket.timeout:
            continue
        g = datagram.raw_datagram(data).decode()
        print('\n\nrecv:',g,end='\n\n')
        if objects.how_ip_name[g['what_how']] == 'unlock':
            unlock()
        if objects.how_ip_name[g['what_how']] == 'on':
            on()
        if objects.how_ip_name[g['what_how']] == 'off':
            off()

th = threading.Thread(target=net_main,args=())
th.start()

if __name__=='__main__':
    while flag:
        cmd = input("lock>")
        if cmd == 'exit':
            flag = False


   

