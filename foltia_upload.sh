#!/bin/sh

set -x

SD=`echo $(cd $(dirname $0) && pwd)`

sudo umount -f /mnt/foltia >/dev/null 2>&1
sudo mount -t cifs -oguest,vers=1.0,iocharset=utf8 //192.168.99.248/JP-file-style /mnt/foltia
cd /tmp
mkdir -p foltia/lists
mkdir -p foltia/lists/keyword
mkdir -p foltia/lists/anime
cp ${SD}/upload_foltia.py foltia/
cd foltia

export LANG=ja_JP.UTF-8
/usr/bin/python3 upload_foltia.py | sh

cd ${SD}
rm -rf /tmp/foltia
sudo umount /mnt/foltia
