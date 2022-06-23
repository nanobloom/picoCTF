#!/usr/bin/python3

import subprocess

for x in range(1000000):
    child = subprocess.Popen("./bbbbloat", stdin=subprocess.PIPE)
    x = str(x)
    x = x.encode()
    child.communicate(x)