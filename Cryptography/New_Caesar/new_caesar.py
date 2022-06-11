#!/usr/bin/python3

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = string.digits + string.ascii_letters + '_' + '?'
encoded = 'mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj'
encoded = [encoded[i:i+2] for i in range(0, len(encoded), 2)]

for key in ALPHABET:
	assert all([k in ALPHABET for k in key])
	assert len(key) == 1

	b16 = b16_encode(flag)
	enc = ""

	for i, c in enumerate(b16):
		enc += shift(c, key[i % len(key)])

	dictio = dict()

	indexx = 0
		
	for i in flag:
		dictio[i] = enc[indexx] + enc[indexx + 1]
		indexx += 2

	result = []

	for item in encoded:
		for key, value in dictio.items():
			if item == value:
				result.append(key)
	
	if len(result) == len(encoded):
		result = "".join(result)
		print('picoCTF{' + result + '}')
