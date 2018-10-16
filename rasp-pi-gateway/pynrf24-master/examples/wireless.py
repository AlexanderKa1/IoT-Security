#import nrf24
import time
import struct

class packet(dict):
    def __init__(self):
        self['length'] = 18 # 1byte
        self['x'] = 1.8
        self['y'] = 8.3
        self['z'] = 7.4
        self['crc'] = 45435
    def encode(self):
        self['crc']=5562
        
        return bin_packet(struct.pack('BfffL',self['length'],self['x'],self['y'],self['z'],self['crc']))
        
        
class bin_packet(bytes):
    def decode(self):
        p = packet()
        up = struct.unpack('BfffL',self)
        p['length'] = up[0]
        p['x'] = up[1]
        p['y'] = up[2]
        p['z'] = up[3]
        p['crc'] = up[4]
        return p
    

#pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

#radio = nrf24.NRF24(pipe[0],pipe[1],32) # 地址，包长度

#radio.write(b'abcdef')
#data = radio.read(10) # 超时

p = packet()
bp = p.encode()
print(bp)
p = bp.decode()
print(p)
