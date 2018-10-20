import RPi.GPIO

class button:
    def __init__(self,pin,addr):
        self.pin = pin
        self.addr = addr
        RPi.GPIO.setmode(RPi.GPIO.BOARD)
        RPi.GPIO.setup(self.pin,RPi.GPIO.IN,pull_up_down=RPi.GPIO.PUD_DOWN)
        return
    def register(self,callback):
        # def callback(channel):
        RPi.GPIO.add_event_detect(self.pin,RPi.GPIO.RISING,callback=self.callback,bouncetime=200)
        self.user_callback = callback
    def callback(self,channel):
        self.user_callback(self.addr)
    def __del__(self):
        RPi.GPIO.remove_event_detect(self.pin)
        RPi.GPIO.setup(self.pin,RPi.GPIO.IN)

