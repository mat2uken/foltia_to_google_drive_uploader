#!/bin/bash

INTERVAL=3600

while true;
do
	./foltia_upload.sh
	echo "----------------------- sleep ${INTERVAL}s"
	sleep ${INTERVAL}
done
