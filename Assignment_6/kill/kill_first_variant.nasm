section .text

global _start

_start:
	xor ebx, ebx

	mov cl, byte [data]
	mov al, byte [data+1]

	dec ebx
	int 0x80

data: 	db 0x25, 0x09
