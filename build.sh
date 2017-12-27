#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y -q gcc make wget python python-pip pppoe git python-dev
sudo apt-get install -y -q net-tools pppoeconf psmisc
sudo apt-get install -y -q rsyslog

pip install pyinstaller -i http://pypi.douban.com/simple/
pyinstaller -F ./endpoints/hkpon.py
pyinstaller -F ./endpoints/hkpoff.py
pyinstaller -F ./endpoints/hkplog.py
pyinstaller -F ./endpoints/hkpmac.py
pyinstaller -F ./endpoints/hkpsetup.py
