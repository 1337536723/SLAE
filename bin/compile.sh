#!/bin/bash

# This is the compile helper. I modified a bit, just
# to detect the file extension and call nasm or gcc
# accordingly.

filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"

echo "[*] Compiling $filename"

if [ "$extension" = "c" ]; then
	echo "[+] Calling gcc without stack protection"
	gcc -fno-stack-protector -z execstack $1 -o $filename
	# objdump -d ./$filename |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-7 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'
fi

if [ "$extension" = "nasm" ]; then

	echo '[+] Assembling with Nasm ... '
	nasm -f elf32 -o $filename.o $1

	echo '[+] Linking ...'
	ld -o $filename $filename.o

	echo '[+] Done!'
fi
