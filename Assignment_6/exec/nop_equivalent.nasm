global _start

section .text

_start:
	nop
	cmp eax, 0x0
	cmp ebx, 0x0
	cmp ecx, 0x0
	xchg eax, eax
	xchg ebx, ebx
	xchg ecx, ecx
