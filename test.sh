#!/bin/bash
HELLO=$(docker run hellodocker)
HW="HelloWorld"
if [ "$HELLO" == "$HW" ]; then
	exit 0
else
	exit 1
fi;
