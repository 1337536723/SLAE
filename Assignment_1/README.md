# Assignment 1: A TCP Bind shellcode

The first assignment asks to create a TCP Bind shellcode that:
* binds on a specific TCP port
* run a shell on incoming connection

The TCP port must be easily configurable.

Syscall numbers are taken from /usr/include/i386-linux-gnu/asm/unistd_32.h

I prepared two version for this assignment. The _light_ version is a classic
bind shellcode; the port is opened, connection accepted and shell spawend. When
the client close the connection the listening deamon dies as expected. 

The _permanent_ version is a bit sophisticated. There is a 5 connections
backlog support and, when the connection it has been accepted, the main process
forks and a dedicated process spawn execve(). During some assessments I found
useful to have more then a shell on the system, so maybe someone can find this
feature useful too. Of course, this version can't be used in an hostile
environment since the binding process stays alive. To overcome this limitation,
it could be possible, as further improvement, to implement a sleep - wakeup
mechanism to be used for kill every process and terminate the whole shellcode.
However, this is far out of scope of this assignement.

## Directory structure

* ```poc``` directory is for the C versions for bind shellcode. I started from
  the POCs to build the assembler file
* ```asm``` directory is for bind shellcode assembler implementations
* shellcode.c is the file responsible to launch shellcode extracted from assembly files
* v_1.py is a python configurator for the shellcode. It is used to choose the
  binding port and if you want the code for _light_ version or the _resident_ one.

