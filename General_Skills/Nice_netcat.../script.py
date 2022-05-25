#!/usr/bin/python3

import subprocess

process = subprocess.run(['nc', 'mercury.picoctf.net', '35652'], stdout=subprocess.PIPE, text=True)

_string = process.stdout
_string = _string.replace('\n','').rstrip()

_list = _string.split(' ')

for index, item in enumerate(_list):
    _list[index] = chr(int(item))

result = ''.join(_list)

print(result)










