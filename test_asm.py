extern printf
LINUX   equ     80H     ; interupt number for entering Linux kernel
EXIT    equ     1       ; Linux system call 1 i.e. exit ()
section .data
    intfmt: db "%ld", 10, 0

segment .text
    global  main


main:
    push rax
    push rsi
    push rdi
    mov rsi, 10
    mov rdi, intfmt
    xor rax, rax
    call printf
    pop rdi
    pop rsi
    pop rax 
    call os_return      ; return to operating system


os_return:
    mov  rax, EXIT      ; Linux system call 1 i.e. exit ()
    mov  rbx, 0     ; Error code 0 i.e. no errors
    mov rcx, 5
    int  LINUX      ; Interrupt Linux kernel
