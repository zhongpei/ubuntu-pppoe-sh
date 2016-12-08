#!/bin/bash
sed -i "s/http:\/\/archive\.ubuntu\.com/http:\/\/mirrors.163.com/" /etc/apt/sources.list
sed -i "s/http:\/\/us\.archive\.ubuntu\.com/http:\/\/mirrors.163.com/" /etc/apt/sources.list
mkdir -p /etc/ppp/peers/

echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata


cp pap-secrets.tp /etc/ppp/pap-secrets.tp
cp dsl-provider.tp /etc/ppp/peers/dsl-provider.tp
cp -r ./endpoints /endpoints

apt-get update -y

apt-get install -y -q gcc make wget python python-pip pppoe git python-dev
apt-get install -y -q net-tools pppoeconf
apt-get install -y -q rsyslog
pip install -r requestments.txt -i http://pypi.douban.com/simple/ 

#apt-get purge -y -q --auto-remove gcc make
service rsyslog start
