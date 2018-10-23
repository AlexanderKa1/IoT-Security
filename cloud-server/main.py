import socket
import l3_acl
import l7_acl
import ipaddress
import datagram
import objects

s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('2607:f2c0:e344:a01::6665',7000))

#addr_acl = l3_acl.acl()
#app_acl = l7_acl.acl()

def unlock_door():
    g = datagram.dict_datagram()
    g['how'] = objects.how_name_ip['unlock']
    s.sendto(g.encode(),('2607:f2c0:e344:a02::2:3',7000))

rule = [
       ('permit','scan','any','entrance_rfid','any',unlock_door)
       ]
def match(rule,x):
    if a=='any':
        return True
    else if a == b:
        return True
    else:
        return False

def l7_acl(g):
    what = objects.what_[g['what']]
    when = g['when']
    where = objects.objects_ip_name[str(g['where'])]
    which = objects.objects_ip_name[str(g['which'])]
    for line in rule:
        if match(line[1],what) and match(line[2],when) and match(line[3],what) and match(line[4],what):
            if line[0] == 'permit':
                line[5]()
            else:
                pass

def l3_acl(addr):
    if addr[0] == '2607:f2c0:e344:a02::2:3':
        return True
    else:
        return False

while True:
    data,addr = s.recvfrom(1000)
    g = datagram.raw_datagram(data).decode()
    if l3_acl(addr) == False:
        continue
    l7_acl(g)
        
    

