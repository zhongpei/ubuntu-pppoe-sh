#!coding: utf-8
"""
Usage:
    hkpon  <username> <password> [--interface=<interface>] [--output=<output>] 

Options:
    -h --help                   Show help
    -i --interface=<interface>  pppoe interface [default: eth1]
    -o --output=<output>        output file
"""

import sys
from docopt import docopt
import time
from command import Commander
import logging


def writeconf(template,target,**kw):

    with open(template) as f:
        data = f.read()
        with open(target,"w+") as f:
            f.write(data.format(**kw))
            return True
    return False

def init_pppoe(args , status_loop = 60):
    c = Commander()
    c.command2("poff -a 2 > /dev/null")
    c.command2("killall -9 pppoe 2 > /dev/null")

    if args.get("<username>") is None:
        logging.error("not have pppoe-username")
        return False,"pppoe param error"
    if args.get('<password>') is None:
        logging.error("not have password")
        return False,"pppoe param error"
    ok = writeconf("/etc/ppp/peers/dsl-provider.tp","/etc/ppp/peers/dsl-provider",username=args["<username>"],interface=args["--interface"])
    if not ok:
        logging.error("write conf /etc/ppp/peers/dsl-provider failed")
        return False,"write conf /etc/ppp/peers/dsl-provider failed"


    ok = writeconf("/etc/ppp/pap-secrets.tp","/etc/ppp/pap-secrets",username=args["<username>"],password=args['<password>'])
    if not ok:
        logging.error("write conf /etc/ppp/pap-secrets failed")
        return False,"write conf /etc/ppp/pap-secrets failed"

    c = Commander()
    rd, ed = c.command2("pon dsl-provider")
    if len(ed) > 0:
        logging.error("pon failed")
        return False,"pon failed"

    for i in range(status_loop):
        ok,why = is_pppoe_conneced()
        logging.info("pppoe {ok}({why})".format(ok=ok,why=why))
        if ok:
            return True,why
        time.sleep(1)
    return False,"pppoe error"

def is_pppoe_conneced():
    c = Commander()
    rd, ed = c.command2("plog")
    for l in rd.split("\n"):
        index = l.find("local  IP address")
        if index != -1:
            ip =  l[index+len("local  IP address"):].strip()
            return True,ip
    return False,"error"

def output(args,**kw):
    output = args.get("--output")
    if output is None:
        return False
    with open(output,"a+") as f:
        for k,v in kw.items():
            f.write("{key} : {value}\n".format(key=k,value=v))
        f.write("\n")
    return True


if __name__ == '__main__':
    args = docopt(__doc__)
    logging.basicConfig(
            level=logging.DEBUG,
            format='%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
    )
    print args
    ok,why = init_pppoe(args)
    output(args,pppoe=ok,ip=why)

    sys.exit()
