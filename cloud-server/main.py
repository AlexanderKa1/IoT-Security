import socket
import l3_acl
import l7_acl
s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('::',7000))

#addr_acl = l3_acl.acl()
#app_acl = l7_acl.acl()

what = {\
        1001:'scan',\
        1002:'push'\
        }

how = {\
        'unlock':2001,\
        'on':2002\
        }
 
while True:
    data,addr = s.recvfrom(1000)
    #addr_acl.acl(addr)
    #app_acl.acl(data)
    #
    if addr[0] == '2607:f2c0:e344:a02::3:2':
        #|---------------------128 bits--------------------|#

        # ------------------------------------------------- #
        #|ver|length |   length   |       datagram ID      |#
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
        print([what[pack[0]],pack[1],pack[2],pack[3],pack[4]])#[what,when,where,which/who,appendix]
        s.sendto(str([1]).encode(),('2607:f2c0:e344:a02::2:3',7000))

    if addr[0] == '2607:f2c0:e344:a02::2:2':
        pack = eval(data.decode())
        print([what[pack[0]]])#[what,when,where,which/who,appendix]
        s.sendto(str([1]).encode(),('2607:f2c0:e344:a02::2:3',7000))

