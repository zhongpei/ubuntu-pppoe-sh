#!/bin/bash
sed -i "s/http:\/\/archive\.ubuntu\.com/http:\/\/mirrors.163.com/" /etc/apt/sources.list
mkdir -p /etc/ppp/peers/

echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata


cp pap-secrets.tp /etc/ppp/pap-secrets.tp
cp dsl-provider.tp /etc/ppp/peers/dsl-provider.tp


apt-get update -y

apt-get install -y -q gcc make wget python python-pip pppoe
apt-get install -y -q net-tools pppoeconf
apt-get install -y -q rsyslog
pip install -r requestments.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

apt-get purge -y -q --auto-remove gcc make wget
service rsyslog start
