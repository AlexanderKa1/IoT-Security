import bsp
import time

def click(x):
    x.on()
    time.sleep(0.2)
    x.off()

click(bsp.sw_module[0])
time.sleep(1)
click(bsp.sw_module[1])
