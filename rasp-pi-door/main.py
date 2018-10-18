import bsp
import time
import rfid

def click(x):
    x.on()
    time.sleep(0.2)
    x.off()

p = rfid.rfid()
while True:
    p.wait()
    key_id,name = p.read()
    if name == 'Alice':
        click(bsp.sw_module[0])
    if name == 'Bob':
        click(bsp.sw_module[1])
    time.sleep(1)
