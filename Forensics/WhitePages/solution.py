#!/usr/bin/python3

with open('whitepages.txt', 'rb') as f:
    text = f.read()

text = text.replace(b'\xe2\x80\x83', b'0')
text = text.replace(b'\x20', b'1')
text = text.decode('ascii')

text = [chr(int(text[i:i+8], 2)) for i in range (0, len(text), 8)]

result = ''.join(text)
result = result.split('\n')[-2]
result = result.lstrip()
print(result) 