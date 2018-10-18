import bsp
import time


bsp.switch_module[0].on()
time.sleep(0.2)
bsp.switch_module[0].off()


