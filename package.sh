#!/bin/bash

rm -fr ./hkppp
mkdir -p hkppp/etc/ppp/peers
mkdir -p hkppp/usr/local/sbin
mkdir -p hkppp/DEBIAN
cp ./pap-secrets.tp hkppp/etc/ppp/peers
cp ./control hkppp/DEBIAN
cp ./dist/* hkppp/usr/local/sbin/
dpkg-deb --build hkppp
