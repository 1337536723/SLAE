# Assignment 3: The Egg Hunter shellcode

## Objectives
In this assignment, I have to:

* study about the Egg Hunter shellcode
* implement a working Egg Hunter PoC in assembler
* have the PoC easily configurable with different payloads 

## The Egg Hunter tecnique

Imagine you find a buffer overflow but you have a very limited space in bytes
to store your attack payload.

The idea behind egg hunting is to store elsewhere your payload prepending it
with a signature, repeated twice. Such a signature is the _egg_. The first
stage is then a code that searches in memory for the signature and, when found,
pass the control to the real payload.

The key before the payload is inserted twice in order to:

* avoid collisions, making sure the hunter found the real egg and not a legit
  bytes sequence that eventually is the same of the key
* optimize the hunter, because it simple to implement the control for equality
  between two contiguous regions of memory

Choosing a good key is also important. We can choose a funny key like
_0xdeadbeef_ or _0x13371337_ and when found in memory jump 8 bytes onward to go
into the real payload or, more optimized by risky in terms of collisions,
# Assignment 3: The Egg Hunter shellcode

## Objectives
In this assignment, I have to:

* study about the Egg Hunter shellcode
* implement a working Egg Hunter PoC in assembler
* have the PoC easily configurable with different payloads 

## The Egg Hunter tecnique

Imagine you find a buffer overflow but you have a very limited space in bytes
to store your attack payload.

The idea behind egg hunting is to store elsewhere your payload prepending it
with a signature, repeated twice. Such a signature is the _egg_. The first
stage is then a code that searches in memory for the signature and, when found,
pass the control to the real payload.

The key before the payload is inserted twice in order to:

* avoid collisions, making sure the hunter found the real egg and not a legit
  bytes sequence that eventually is the same of the key
* optimize the hunter, because it simple to implement the control for equality
  between two contiguous regions of memory

Choosing a good key is also important. We can choose a funny key like
_0xdeadbeef_ or _0x13371337_ and when found in memory jump 8 bytes onward to go
into the real payload or, more optimized by risky in terms of collisions,
choose a key that makes sense in assembler.

The paper "Safetly searching Process Virtual Address Space", use the 0x90509050
as key. Such a key in assembler is translated in:

> 90	; nop
> 50	; push eax 
> 90	; nop
> 50	; push eax 

I'd rather prefer having a customizable key, so I'll put in my egg hunter data
section, threating it as it would not make sens in assembler.

### References

[Safetly searching Process Virtual Address Space](http://www.hick.org/code/skape/papers/egghunt-shellcode.pdf)
https://www.corelan.be/index.php/2011/01/09/exploit-writing-tutorial-part-8-win32-egg-hunting/
https://www.exploit-db.com/exploits/17559/

[Post on CodiceInsicuro](https://codiceinsicuro.it/slae/assignment-3-an-egg-hunter-journey/)
[Post on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:6407580755962191872)
[Shellcode on Exploit-DB](https://www.exploit-db.com/exploits/44807/)
