---
parent file:
  - "[[Root]]"
related: "[[The Art of 64-Bit Assembly]]"
creation data: 2023-12-06, 07:43
tags:
  - "#guides"
  - "#research"
  - "#code"
---
# Introduction to Arm Assembly Basics

The series is focused on the basics of ARM with the perspective of writting shell code for the platform [^Azeria]

- ARM is a RISC (reduced instruction set computing) but with their own licensing. So while ARM requires licensing fees to use their IP RISCV has no restrictions [^RISCV_About]

Advantages and disadvantages 
- unlike Intel, ARM has 100 or less instructions and more general purpose registers [^Azeria]
- Unlike x86, ARM is big-endian with the option of switching making it BI-Endian 
- ARM also has two modes, ARM mode and Thumb mode 

ARM versions [^Azeria]
![[Pasted image 20231207095750.png]]

## What is assembly 
- assembly is a thin layer of syntax on top of machine code which is composed of instructions 
- to be able to write assembly you need a program to convert the assembly language to machine code. An example of that is the gnu assembler. We will then need to link it which probably adds a runtime if I am not mistaken. 
```bash
as program.s -o program.o
ld program.o -o program
```

The code above is automatically accomplished by a compiler

```bash
gcc program.c -o program 
```

## Assembly Syntax
The syntax of assembly is broken down into `mnemonics` `operand` for example 
```asm 
MOV R1, R2
```

---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 
[^Azeria]: https://azeria-labs.com/writing-arm-assembly-part-1/
[^RISCV_About]: https://youtu.be/vaMxTSm53UU?si=Z2ljLs0UDjKvLuu2



[Azeria Intro to ARM Assembly Basics](https://azeria-labs.com/writing-arm-assembly-part-1/)