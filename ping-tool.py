#!/usr/bin/python
# -*- coding: utf-8 -*-

import pings
import time
import json
import sys

def ping_test(host):
    with open("./store.txt","r+") as f:
        if f.read()=="":
            result=str(time.time())+":"+str(pings.Ping().ping(host))
        else:
            result=" , "+str(time.time())+":"+str(pings.Ping().ping(host))
        f.write(f.read()+result)

try:
    hostname=sys.argv[1]
    ping_test(hostname)
except IndexError: 
    print("Geben Sie einen Host an, der gepingt werden soll.")
except IOError:
    print("Navigieren Sie zum Ausführen bitte in den Programmordner.")
