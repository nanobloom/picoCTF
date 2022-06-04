#!/usr/bin/python3

import os
import hashlib

if 'keygenme-trial.py' not in os.listdir():
    print('keygenme-trial.py must be in the same directory')
    exit()

i = 0

with open('keygenme-trial.py', 'r') as f:
    for line in f.readlines():
        if line.startswith('username_trial'):
            username = line.split("\"")[1]
            i += 1
        if line.startswith('key_part_static1_trial'):
            part1 = line.split("\"")[1]
            i += 1
        if line.startswith('key_part_static2_trial'):
            part3 = line.split("\"")[1]
            i += 1
        if i > 2:
            break

hash = hashlib.sha256(username.encode('utf-8')).hexdigest()
part2 = hash[4] + hash[5] + hash[3] + hash[6] + hash[2] + hash[7] + hash[1] + hash[8]

result = f"{part1}{part2}{part3}"
print(result)

