#!/usr/bin/python3
#-----------------------------------------------------------------#
#                               Ark Sun                           #
#                             2018-10-20                          #
#                        arksun9481@gmail.com                     #
#-----------------------------------------------------------------#

import socket
import ipaddress
import datagram
import objects
import time
import ipsec
import select
import threading
import sys
import queue
bind_addr = ('2607:f2c0:e344:a01::6665',7000)

s = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(bind_addr)
s.settimeout(0.5)

s2 = ipsec.ipsec_socket(socket.AF_INET6,socket.SOCK_RAW,socket.IPPROTO_ESP)
s2.bind((bind_addr[0],0))
s2.connect(('2607:F2C0:E344:A02:260A:C4FF:FE0F:C338',0))

rule = [
       ('permit',('scan','any','entrance_rfid','any'),('unlock','now','entrance_lock','entrance_lock')),
       ('permit',('push','any','gateway_buttons','gateway_buttons_3'),('unlock','now','entrance_lock','entrance_lock')),
       ('permit',('push','any','gateway_buttons','gateway_buttons_0'),('off','now','light_relay','light_relay')),
       ('permit',('push','any','gateway_buttons','gateway_buttons_1'),('on','now','light_relay','light_relay')),
       ('deny',('scan','any','entrance_rfid','any')),
       ]

rules = {'default':rule}

def action(a):
    g = datagram.dict_datagram()
    g['flags'] = 1
    g['what_how'] = objects.how_name_ip[a[0]]
    g['when'] = 0.
    g['where'] = ipaddress.IPv6Address(objects.objects_name_ip[a[2]])
    g['which_who'] = ipaddress.IPv6Address(objects.objects_name_ip[a[3]])
    if a[2] == 'light_relay':
        try:
            s2.send(g.encode())
        except:
            print('s2 failed')
    else:
        try:
            s.sendto(g.encode(),(str(g['where']),7000))
        except:
            print('s failed')

def match(r,x):
    if r=='any':
        return True
    elif r == x:
        return True
    elif r=='weekday':
        weekday = {'Monday','Tuesday','Wednesday','Thursday','Friday'}
        if time.strftime("%A",time.localtime(x)) in weekday:
            return True
        else:
            return False
    elif r=='weekends':
        weekend = {'Saturday','Sunday'}
        if time.strftime("%A",time.localtime(x)) in weekend:
            return True
        else:
            return False
    elif r=='9am4pm':
        if int(time.strftime("%H",time.localtime(x))) in range(9,16):
            return True
        else:
            return False
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
                    action(line[2])
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
    if addr[0] in l3_rule:
        return True
    else:
        return False

flag = True

def net_main():
    global s,net_queue,flag
    while flag:
        try:
            data,addr = s.recvfrom(1000)
        except socket.timeout:
            continue
        g = datagram.raw_datagram(data).decode()
        g['when'] = time.time()
        if l3_acl(addr) == False:
            continue
        l7_acl(g)

def split(cmd):
    global rule,rules
    cmd = list(cmd)
    res = []
    buff = ''
    for i in cmd:
        if i == ' ':
            if buff != '':
                res.append(buff)
                buff = ''
        else:
            buff+=i
    if buff != '':
        res.append(buff)
        buff = ''
    return res

def server(a):
    global flag
    if a == []:
        return 'server'
    if a[0] == 'show':
        return 'server'
    if a[0] == 'exit':
        flag = False
        return 'server'
    if a[0] == 'acl':
        return 'acl'
    return 'server'

rule_now = 'default'
edit = 'default'
def acl(a):
    global rules,rule,rule_now,edit
    if a == []:
        return 'acl'
    if a[0] == 'show':
        print('rule now:',rule_now)
        print('editing:',edit)
        print('rules:\n')
        for i in rules:
            print(i,':')
            for j in rules[i]:
                print(j)
        print('\n\nSyntex: [permit/deny] [what] [when] [where] [which] [how] [when] [where] [which]')
        return 'acl'
    if a[0] == 'permit':
        rules[edit].append(('permit',tuple(a[1:5]),tuple(a[5:9])))
    if a[0] == 'deny':
        rules[edit].append(('deny',tuple(a[1:5])))
    if a[0] == 'del':
        del rules[a[1]]
    if a[0] == '?':
        print('    acl       apply acl to the server')
        print('    edit      edit acl')
        print('    permit    permit rule')
        print('    deny      deny rule')
        print('    del       del acl')
        print('    exit      exit to last menu')
        print()
    if a[0] == 'edit':
        edit = a[1]
        if a[1] not in rules:
            rules[a[1]]=[]
    if a[0] == 'exit':
        return 'server'
    if a[0] == 'acl':
        rule = rules[a[1]]
    return 'acl'

def cli_main():
    global flag
    s = '>'
    menu = {'server':server,'acl':acl}
    menu_now = 'server'
    while flag:
        a = input(menu_now+s)
        a = split(a)
        menu_now = menu[menu_now](a)

if __name__=='__main__':
    print('#**************************************#')
    print('#IoT server                            #')
    print('#Author: Ark Sun                       #')
    print('#E-mail:arksun9481@gmail.com           #')
    print('#**************************************#')
    print()
    print('Initializing network')
    net_queue = queue.Queue()
    cli_queue = queue.Queue()
    net_th = threading.Thread(target=net_main,args=())
    print('Initializing cli')
    cli_th = threading.Thread(target=cli_main,args=())
    net_th.start()
    cli_th.start()

