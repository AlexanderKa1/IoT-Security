#!/usr/bin/env python
#---------------------------------------------------#
#                    Author:Ark Sun                 #
#                      2018-10-18                   #
#                arksun9481@gmail.com               #
#---------------------------------------------------#

import signal
import time
import sys
import threading
import logging
from pirc522 import RFID

class rfid:
    def __init__(self):
        self.run_flag = True
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = True
        self.fifo = []
        self.db = {(70,57,222,19,178):'Alice',(70,131,51,20,226):'Bob'}
        signal.signal(signal.SIGINT, self.end_read)
        print("Starting")
    def wait(self):
        self.rdr.wait_for_tag()
    def read(self):
        (error, data) = self.rdr.request()
        if not error:
            print("Detected: " + format(data, "02x"))
        else:
            print("Error")
            return ((0,0,0,0,0),'error')
        (error, uid) = self.rdr.anticoll()
        if not error:
            key_id = tuple(uid)
            print("Card read UID: ",key_id,self.db[key_id])
            return (key_id,self.db[key_id])
        else:
            print("Error")
            return ((0,0,0,0,0),'error')
    def run(self,callback):
        self.th = threading.Thread(target = self.thread,args = (callback,))
        self.th.run()
    def thread(self,callback):
        self.last = None
        while self.run_flag:
            self.wait()
            res = self.read()
            if res[0] != self.last[0]:
                callback(*res)
                self.last = res
            time.sleep(0.1)
    def end_read(signal,frame):
        print("Ctrl+C captured, ending read.")
        self.run_flag = False
        self.rdr.cleanup()
        sys.exit()



