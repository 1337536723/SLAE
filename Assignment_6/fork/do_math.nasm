global _start

section .text

_start:
	sub	eax, eax
	mov	al, 0xF3
	sub	al, 0xE2

	sub 	ebx, ebx
	sub 	ecx, ecx
	sub 	edx, edx

	andn	ebx, ebx, ebx
	andn	ecx, ecx, ecx
	andn	edx, edx, edx

	add ebx, 0x4
	add ecx, 0x5
	add edx, 0x6

	sub ebx, 0x4
	sub ecx, 0x5
	sub edx, 0x6

	push 0x3
	pop ebx

	push 0x4
	pop ecx

	push 0x5
	pop edx
