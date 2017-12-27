#!/bin/bash

rm -fr ./hkppp
mkdir -p hkppp/usr/local/sbin
mkdir -p hkppp/DEBIAN
cp ./control hkppp/DEBIAN
cp ./dist/* hkppp/usr/local/sbin/
dpkg-deb --build hkppp
