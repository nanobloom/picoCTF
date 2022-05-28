#!/usr/bin/python3

with open('enc', 'r') as txt:
    enc = txt.read()

_list = []

for i in enc:
    a = hex(ord(i)).lstrip('0x')
    _list.append(chr(int(a[:2],16)))
    _list.append(chr(int(a[2:],16)))

result = "".join(_list)
print(result)

