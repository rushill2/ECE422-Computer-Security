.global _main
.section .text

# unused buggy declaration for code
file_shell:
 .ascii "/bin/sh"


_main:

push    %ebp
mov     %esp,%ebp

# clearing out unused arguments
mov $0, %esi
mov $0, %edi
mov $0, %ebp

# system call code 11 for sysexecve
mov $11, %eax

# setting up filename
push $0x68732f
push $0x6e69622f
# move pointer to /bin/sh string to ebx as first argument
mov %esp, %ebx 

# getting pointers to 0/null values for envp and argv
push $00
mov %esp, %ecx

push $00
mov %esp, %edx

# syscall 
int $0x80

leave
ret
