import bsp
import time
import threading
import os
import socket

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

how = {0:nothing,1:unlock,2:on,3:off}

def click(x):
    x[0].on()
    x[1].on()
    time.sleep(0.2)
    x[0].off()
    x[1].off()
#-----------------------------------------------------------------------
output = os.popen('ip -6 addr add 2607:f2c0:e344:a02::2:3/64 dev wlan0')
print(output.read())
time.sleep(2)
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('2607:f2c0:e344:a02::2:3',7000))
#-----------------------------------------------------------------------
while True:
    data = s.recv(1000)
    pack = eval(data.decode())
    print(pack)
    how[pack[0]]()

