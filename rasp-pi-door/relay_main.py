import bsp
import time
import threading
import os
import socket

def click(x):
    x[0].on()
    x[1].on()
    time.sleep(0.2)
    x[0].off()
    x[1].off()

output = os.popen('ip -6 addr add 2607:f2c0:e344:a02::2:3/64 dev wlan0')
print(output.read())
time.sleep(2)
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('2607:f2c0:e344:a02::2:3',7000))

while True:
    data = s.recv(100)
    print('recv:',data)
    if data.decode() == 'Alice':
        click(bsp.sw_module)
    if data.decode() == 'Bob':
        click(bsp.sw_module)

