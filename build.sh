#!/bin/bash
pip install pyinstaller -i http://pypi.douban.com/simple/
pyinstaller -F ./endpoints/hkpon.py
pyinstaller -F ./endpoints/hkpoff.py
pyinstaller -F ./endpoints/hkplog.py
pyinstaller -F ./endpoints/hkpmac.py
pyinstaller -F ./endpoints/hkpsetup.py
