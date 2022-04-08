.global your_asm_fn
.section .text

your_asm_fn:

push    %ebp
mov     %esp,%ebp


# pushing null terminated ascii type string onto stack to get pointer
push $00
push $0x646f6f66
push $0x6c6f6f63

# getting pointer to string
mov %esp, %edx

# getting pointer to closed
push $0xc105ed
mov %esp, %ebx

# pushing all arguments in right to left order
push %edx
push %ebx
push $0xacce55ed

call practice

leave
ret
