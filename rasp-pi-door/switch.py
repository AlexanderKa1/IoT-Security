import RPi.GPIO

class switch:
    def __init__(self,pin):
        self.pin = pin
        RPi.GPIO.setmode(RPi.GPIO.BOARD)
        RPi.GPIO.setup(self.pin,RPi.GPIO.OUT)
        RPi.GPIO.output(self.pin,RPi.GPIO.HIGH)
        return
    def on(self):
        RPi.GPIO.output(self.pin,RPi.GPIO.LOW)
    def off(self):
        RPi.GPIO.output(self.pin,RPi.GPIO.HIGH)
    def __del__(self):
        RPi.GPIO.setup(self.pin,RPi.GPIO.IN)

