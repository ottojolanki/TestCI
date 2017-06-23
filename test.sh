#!/bin/bash
HELLO=$(docker run hellodocker)
HW="HelloWorl"
if [ "$HELLO" == "$HW" ]; then
	exit 0
else
	exit 1
fi;
