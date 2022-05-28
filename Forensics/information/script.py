#!/usr/bin/python3

import subprocess
import base64

process = subprocess.run(['exiftool', 'cat.jpg'], stdout=subprocess.PIPE, text=True)

_string = process.stdout
_string = _string.split('License')[1]
_string = _string.split('Rights')[0]
_string = _string.lstrip(': ')

decodedBytes = base64.b64decode(_string)
result = str(decodedBytes, 'utf-8')

print(result)
