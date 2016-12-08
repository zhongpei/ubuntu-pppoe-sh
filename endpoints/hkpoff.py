#!coding: utf-8
"""
Usage:
    hkpoff

Options:
    -h --help                   Show help
"""

import sys
from docopt import docopt
import time
from command import Commander
import logging

if __name__ == "__main__":
    c = Commander()
    c.command2("poff -a")
    c.command2("killall -9 pppoe")
    rd, ed = c.command2("plog -n 20")
    print rd
