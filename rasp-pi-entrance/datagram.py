#***************************************************#
#                       Ark Sun                     #
#                     2018-10-23                    #
#                 arksun9481@gmail.com              #
#***************************************************#


#|---------------------128 bits--------------------|#

# ------------------------------------------------- #
#|ver| flags |   length   |       datagram ID      |#
# ------------------------------------------------- #
#|          what          |           when         |#
# ------------------------------------------------- #
#|                      where                      |#
# ------------------------------------------------- #
#|                    which/who                    |#
# ------------------------------------------------- #
#|                    appendix                     |#
# ------------------------------------------------- #



#|--------------------flags 32bits-----------------|#

# ------------------------------------------------- #
#|                                        |what/how|#
# ------------------------------------------------- #

import ipaddress


class raw_datagram(bytes):
    def decode(self):
        datagram = dict_datagram()
        datagram['ver'] = int.from_bytes(self[0:2],'little')
        datagram['flags'] = int.from_bytes(self[2:4],'little')
        datagram['length'] = int.from_bytes(self[4:8],'little')
        datagram['datagram_ID'] = int.from_bytes(self[8:16],'little')
        datagram['what_how'] = int.from_bytes(self[16:24],'little')
        datagram['when'] = struct.unpack('<d',self[24:32])[0]
        datagram['where'] = ipaddress.IPv6Address(self[32:48])
        datagram['which_who'] = ipaddress.IPv6Address(self[48:64])
        datagram['appendix'] = self[64:80]
        return datagram

class dict_datagram(dict):
    def __init__(self):
        self['ver'] = 100
        self['flags'] = 0
        self['length'] = 80
        self['datagram_ID'] = 0
        self['what_how'] = 0
        self['when'] = 0.
        self['where'] = ipaddress.IPv6Address('::')
        self['which_who'] = ipaddress.IPv6Address('::')
        self['appendix'] = b'\x00'*16
    def encode(self):
        ver = self['ver'].to_bytes(2,'little')
        flags = self['flags'].to_bytes(2,'little')
        length = self['length'].to_bytes(4,'little')
        datagram_ID = self['datagram_ID'].to_bytes(8,'little')
        what_how = self['what_how'].to_bytes(8,'little')
        when = struct.pack('<d',self['when'])
        where = self['where'].packed
        which_who = self['which_who'].packed
        appendix = self['appendix']
        return raw_datagram(ver+flags+length+datagram_ID+what_how+when+where+which_who+appendix)



    
