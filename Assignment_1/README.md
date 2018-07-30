# Assignment 1: A TCP Bind shellcode

The first assignment asks to create a TCP Bind shellcode that:
* binds on a specific TCP port
* run a shell on incoming connection

The TCP port must be easily configurable.

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

## On the internet
 
[Post on CodiceInsicuro](https://codiceinsicuro.it/slae/assignment-1-create-a-bind-shellcode/)
[Shellcode on Exploit-DB](https://www.exploit-db.com/exploits/44808/)
