#!/usr/bin/env python
# Revised Connection Example - Chapter 2 - connect2.py
import socket

print("Creating socket . . .")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("done.")
except:
    print("failed to create socket.")

print("Looking up port number . . .")
try:
    port = socket.getservbyname('http', 'tcp')
    print("done.")
except:
    print("failed to look up port number.")

print("Connecting to remote host on port %d . . ." %(port))
try:
    s.connect(("www.google.com", port))
    print("done.")
except:
    print("failed to connect remote host on port.")