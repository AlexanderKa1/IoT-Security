import socket
import l3_acl
import l7_acl
import ipaddress
import datagram
import objects
import time

s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('2607:f2c0:e344:a01::6665',7000))

def unlock_door():
    global s
    print('matched')
    g = datagram.dict_datagram()
    g['what_how'] = objects.how_name_ip['unlock']
    print(g)
    s.sendto(g.encode(),('2607:f2c0:e344:a02::2:3',7000))


rule = [
       ('permit',('scan','any','entrance_rfid','ark_card'),unlock_door),
       ('permit',('scan','any','entrance_rfid','ark_card'),('unlock','now','entrance_lock','entrance_lock')),
       ('deny',('scan','any','entrance_rfid','any')),
       ]

def match(r,x):
    if r=='any':
        return True
    elif r == x:
        return True
    else:
        return False

def match_id(x,y):
    if match(x[0],y[0]) and match(x[1],y[1]) and match(x[2],y[2]) and match(x[3],y[3]):
        return True
    else:
        return False

def l7_acl(g):
    what = objects.what_ip_name[g['what_how']]
    when = g['when']
    where = objects.objects_ip_name[str(g['where'])]
    which = objects.objects_ip_name[str(g['which_who'])]
    for line in rule:
        if match_id(line[1],(what,when,where,which)):
            if line[0] == 'permit':
                if type(line[2]) == tuple:
                    pass
                else:
                    line[2]() 
                print((what,when,where,which),'-> permitted:',line[1],line[2])
            else:
                print((what,when,where,which),'-> denied:', line[1])
            break
    



l3_rule = {'2607:f2c0:e344:a02::2:2',
           '2607:f2c0:e344:a02::2:3',
           '2607:f2c0:e344:a02::3:2'}


def l3_acl(addr):
    if addr[0] == '2607:f2c0:e344:a02::2:2':
        return True
    else:
        return False

while True:
    data,addr = s.recvfrom(1000)
    g = datagram.raw_datagram(data).decode()
    g['when'] = time.time()
    if l3_acl(addr) == False:
        continue
    l7_acl(g)
        
    

