#!/bin/sh

set -x

SD=`echo $(cd $(dirname $0) && pwd)`

export PATH=$PATH:/usr/local/bin

sudo umount -f /mnt/foltia >/dev/null 2>&1
sudo mount -t cifs -oguest,vers=1.0,iocharset=utf8 //192.168.99.11/JP-file-style /mnt/foltia
cd /tmp
mkdir -p foltia2/lists
mkdir -p foltia2/lists/epg
mkdir -p foltia2/lists/keyword
mkdir -p foltia2/lists/anime
cp ${SD}/upload_foltia.py foltia2/
cd foltia2

export LANG=ja_JP.UTF-8
/usr/bin/python3 upload_foltia.py | sh
#/usr/bin/python3 upload_foltia.py

cd ${SD}
rm -rf /tmp/foltia
sudo umount /mnt/foltia
