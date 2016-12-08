#!coding: utf-8
"""
Usage:
    hkplog

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
    rd, ed = c.command2("plog -n 20")
    print rd
