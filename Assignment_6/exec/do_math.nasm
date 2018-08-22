global _start

section .text

_start:
	sub	eax, eax
	mov	al, 0xF3
	sub	al, 0xE2

	sub 	ecx, ecx
	sub 	edx, edx
	andn	ecx, ecx, ecx
	andn	edx, edx, edx

	push 0x3
	pop ecx
	sub cl, 0x3

	push 0x7F
	pop edx
	sub dl, 0x7F
