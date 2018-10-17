import machine

class switch:
    def __init__(self,pin):
        self.pin = machine.Pin(pin,machine.Pin.OUT)
        self.pin.value(1)
        return
    def on(self):
        self.pin.value(0)
    def off(self):
        self.pin.value(1)
    def __del__(self):
        self.pin = machine.Pin(self.pin,machine.Pin.IN)

