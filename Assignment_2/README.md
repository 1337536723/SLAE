# Assignment 2: A TCP Reverse shell shellcode

The second assignment asks to create a TCP reverse shell shellcode that:
* reverse connects on a specified IP and PORT
* execs a shell on successfull connection

The IP address TCP port must be easily configurable.

Syscall numbers are taken from /usr/include/i386-linux-gnu/asm/unistd_32.h

The assignment solution is a classic bind shellcode; the port is opened,
connection accepted and shell spawend. When the client close the connection the
listening deamon dies as expected. 

## Directory structure

* ```poc``` directory is for the C versions for bind shellcode. I started from
  the POCs to build the assembler file
* ```asm``` directory is for bind shellcode assembler implementations
* shellcode.c is the file responsible to launch shellcode extracted from assembly files
* venom_a1.py is a python configurator for the shellcode. It is used to choose the
  binding port

