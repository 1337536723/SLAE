/*
 * Put your assembler file here
 */

#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"SHELLCODE";

		       
int main(int argc, char **argv)
{
	printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}

	
