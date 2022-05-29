#!/usr/bin/python3

f = open('mystery', 'rb')

data = list(f.read())

for index, item in enumerate(data):
    data[index] = hex(item)

f.close()

# Fixing magic number
data[1] = '0x50'  # P
data[3] = '0x47'  # G
data[6] = '0x1A'  # Required for OS compatibility
data[7] = '0x0A'  # Required for OS compatibility

# Fixing image header (IHDR)
data[12] = '0x49' # I
data[13] = '0x48' # H

# Fixing pixel width (pHYs chunk)
data[70] = '0x00' # otherwise width would be 2852132389 pixels

# Fixing IDAT chunk data size
data[83] = '0x00'
data[84] = '0x00'

# Fixing IDAT chunk name
data[87] = '0x49' # I
data[89] = '0x41' # A

for index, item in enumerate(data):
    data[index] = int(item, 16)

f2 = open('result.png', 'wb')

f2.write(bytes(data))

f2.close()
