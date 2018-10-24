import button
import ipaddress

ipv6 = ipaddress.IPv6Address

buttons_addr = [\
        ipv6('2607:f2c0:e344:a03:3::1:0'),\
        ipv6('2607:f2c0:e344:a03:3::1:1'),\
        ipv6('2607:f2c0:e344:a03:3::1:2'),\
        ipv6('2607:f2c0:e344:a03:3::1:3')\
    ]
buttons_pins = [37,35,33,31]

buttons_mo = [button.button(buttons_pins[i],buttons_addr[i]) for i in range(4)]


