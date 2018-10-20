import socket
import l3_acl
import l7_acl
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('::',7000))

#addr_acl = l3_acl.acl()
#app_acl = l7_acl.acl()

while True:
    data,addr = s.recvfrom()
    #addr_acl.acl(addr)
    #app_acl.acl(data)
    if addr == ('2607:f2c0:e344:a02::3:2',7000):
        #|---------------------128 bits--------------------|#

        # ------------------------------------------------- #
        #|ver|    flags    |length|       datagram ID      |#
        # ------------------------------------------------- #
        #|          what          |           when         |#
        # ------------------------------------------------- #
        #|                      where                      |#
        # ------------------------------------------------- #
        #|                    which/who                    |#
        # ------------------------------------------------- #
        #|                    appendix                     |#
        # ------------------------------------------------- #
        pack = eval(data.decode())
        print(pack)#[what,when,where,which/who,appendix]
        rule = [1,'any','2607:f2c0:e344:a02::3:2','2607:f2c0:e344:a03::']
        action = [1,0,'2607:f2c0:e344:a02::2:3','::1','?']
        #if pack[1] == 
