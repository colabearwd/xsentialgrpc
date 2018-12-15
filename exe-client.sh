#!/bin/bash

if [ "$1" == 'ping' ]
then
	PYTHONPATH=./gen-py python client/client-ping.py
else
	PYTHONPATH=./gen-py python client/client-curl.py
fi
