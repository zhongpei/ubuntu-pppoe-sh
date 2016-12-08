#!coding: utf-8
"""
Usage:
    hkpmac [interface=<interface>]

Options:
    -h --help                   Show help
    -i --interface=<interface>  pppoe interface [default: eth1]
"""

import sys
from docopt import docopt
import time
from command import Commander
import logging
from random import randint
import datetime

def change_mac(interface):
    mac = "%02x:%02x:%02x:%02x:%02x:%02x" % (randint(1,16),randint(1,16),randint(1,16),randint(1,16),randint(1,16),randint(1,16)) 
    print mac
    c = Commander()
    with open('/etc/ppp/mac_list','a+') as f:
        f.write("%s\t%s\n"%(datetime.datetime.now(),mac))
    c.command2("ifconfig %s down"%interface)
    c.command2("ifconfig %s hw ether %s "%(interface,mac))
    rd, ed = c.command2("ifconfig %s "%interface)
    print rd
    return True

if __name__ == "__main__":
    args = docopt(__doc__)
    interface = args.get("--interface","eth1")
    change_mac(interface)

