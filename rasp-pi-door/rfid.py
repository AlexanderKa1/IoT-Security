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
        self.db =\
                {\
                (0,0,0,0,0):'Error',\
                (70,57,222,19,178):'Alice',\
                (70,131,51,20,226):'Bob',\
                (121,75,196,197,51):'Ark',\
                (99,199,196,197,165):'Eve'\
                }
        signal.signal(signal.SIGINT, self.end_read)
    def wait(self):
        self.rdr.wait_for_tag()
    def read(self):
        (error, data) = self.rdr.request()
        if not error:
            pass # Detected: data
        else:
            return (0,0,0,0,0)
        (error, uid) = self.rdr.anticoll()
        if not error:
            key_id = tuple(uid)
            return key_id
        else:
            return (0,0,0,0,0)
    def run(self,callback):
        self.th = threading.Thread(target = self.thread,args = (callback,))
        self.th.run()
    def thread(self,callback):
        self.last = None
        while self.run_flag:
            t1 = time.time()
            self.wait()
            t2 = time.time()
            if t2 - t1 > 0.1:
                self.last = None
            res = self.read()
            if res != self.last:
                callback(res)
                self.last = res
            time.sleep(0.1)
    def end_read(signal,frame):
        print("Ctrl+C captured, ending read.")
        self.run_flag = False
        self.rdr.cleanup()
        sys.exit()
