#include<stdio.h>
#include<string.h>

unsigned char egg_hunter[] = \
			     "EGG_HUNTER";

unsigned char code[] = \
		       "CODE"; 
int main(int argc, char **argv)
{
	printf("Shellcode Length:  %d\n", strlen(code));
	printf("Egghunter Length:  %d\n", strlen(egg_hunter));
	int (*ret)() = (int(*)())egg_hunter;
	ret();
}

	
