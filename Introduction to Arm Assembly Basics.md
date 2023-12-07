---
parent file:
  - "[[Root]]"
related:
  - "[[The Art of 64-Bit Assembly]]"
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
- Unlike x86, ARM is big-endian with the option of switching making it [[BI-Endian]] 
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
```armasm
MOV R1, R2
```


## Data Types
Just like HLL there are different data types that ARM operations work on. The data types are signed or unsigned `words`, `havewords` and `bytes` [^Azeria]
![[Pasted image 20231207143047.png]]
These data types of extentios associated with them being `-h` or `sh` for halfwords, `b` or `sb` for bytes and no extension for words

Example of how these are used:
```
ldr = Load Word
ldrh = Load unsigned Half Word
ldrsh = Load signed Half Word
ldrb = Load unsigned Byte
ldrsb = Load signed Bytes

str = Store Word
strh = Store unsigned Half Word
strsh = Store signed Half Word
strb = Store unsigned Byte
strsb = Store signed Byte
```

## Endianness
Endianness is the byte-order in which each byte of an object is stored in memory. Little-endian (LE) like x86 is stored where the **least-significant-byte** is stored at the lowest address. Addresses typically grow from bottom to top, were the bottom is the lowest address. Therefore, in little-endian the bytes flow in the oder from bottom to top.

Big-endian on the other hand is the other way around and it is the preferred byte-order of networking data.

Before ARMv3, the architecture was little-endian, since then it has become [[BI-Endian]]. On ARMv6, the instructions are **fixed little-endian** while the **data access** can be either little-endian or big-endian as controlled by bit 9, the **E bit** of the **Program Status Register (CPSR)**

## Registers
The amount of registers depends on the ARM version. According to the ARM reference Manual [^ARM_Manual] there are **30 general-purpose 32-bit registers**. The first 16 registers are accessible in the **user-level mode**. The additional registers are available in privilege software execution. 
![[Pasted image 20231207150414.png]]

![[Pasted image 20231207150542.png]]

**R0-R12** can be used during common operations to store temporary values, pointers, etc. **R0** for example can be referred as **accumulator** during the 


---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 
[^Azeria]: https://azeria-labs.com/writing-arm-assembly-part-1/
[^RISCV_About]: https://youtu.be/vaMxTSm53UU?si=Z2ljLs0UDjKvLuu2
[^ARM_Manual]: https://developer.arm.com/documentation/dui0473/c/Babdfiih


[Azeria Intro to ARM Assembly Basics](https://azeria-labs.com/writing-arm-assembly-part-1/)