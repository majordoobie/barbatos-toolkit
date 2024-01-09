---
parent file:
  - "[[Published]]"
related:
  - "[[Introduction to Arm Assembly Basics]]"
creation data: 2023-12-08, 07:20
tags:
  - "#guides"
  - "#research"
  - "#code"
---
# AArch64
These notes are created by following the guide provided by  [mariokartwii](https://mariokartwii.com/armv8/index.html)

## ARM64 vs AArch64
"AArch64" is the official name, it means "Arm Architecture 64-bit".

"arm64" is an unofficial name some people use because the official name sucks.

Originally there was just the 32-bit architecture, called "ARM". Then [in October 2011](https://en.wikipedia.org/wiki/ARM_architecture_family#Armv8-A) the ARMv8-A spec added a new 64-bit execution state called "AArch64", retroactively renaming the old 32-bit architecture "AArch32". Then to add a bit more confusion, in 2017 the company [rebranded](https://en.wikipedia.org/wiki/Arm_(company)#Name) from being called "ARM" (an acronym for "Advanced RISC Machines") to just "Arm".

Support for AArch64 was added to Linux in 2012. The patchset was initially called "aarch64" but was [renamed](https://lkml.org/lkml/2012/7/6/624) to "arm64". The LLVM community and Apple started working in parallel to support it in clang in 2012, the LLVM community called it "aarch64" and Apple called it "arm64". Apple open-sourced their changes and the two efforts lived together in LLVM under their different names and were eventually [merged in 2014](https://www.phoronix.com/news/MTY5ODk) so LLVM/clang now just calls it "aarch64". ^[https://stackoverflow.com/questions/31851611/differences-between-arm64-and-aarch64#:~:text=%22AArch64%22%20is%20the%20official%20name%2C%20it%20means%20%22Arm%20Architecture%2064%2Dbit%22.]

# Chapter 1: Intro, What is an Assembly Language?
- Binary is interpreted as voltage being present or absent 
- instructions for one CPU will likely not work for another CPU since assembly is CPU specific. This is where things like HLL (High Level Languages) come into play where you can write once and run mostly every where.

What are some advantages to learning assembly? 
- Writing out the Boot/Reset Sequence for a CPU
- Writing out CPU-specific specialized tasks
- Further enhance performance
- Understanding a specific CPU as much as possible
- Exploits/Hacks for a specific CPU (such as for Video Game Consoles)
- A better Understanding of "under the hood" stuff (such as Memory Management, Cache, etc)

# Chapter 3: Navigating Through Memory
The region of memory that programs typically reside is called **static memory** or **main memory**. This is because every time a specific program is executed by the CPU, the CPU instructions are usually placed at the same locations within the **static memory** every single time. 
> I am guessing that they are talking about virtual memory here, not physical

The fixed length of memory addresses are determined by the CPU itself and some special properties of the CPU that are determined/written by a program shortly after said CPU has booted or been reset. Example: `0x80516074`

## Navigating Memory
Typical memory outputs are dumped in hex with 16 bytes across. Since they are 16 bytes across, each row increments by 16 bytes or `0x10` making it easier to visualize the increments. So, if you want to find address `0x80516074`, you start from the stop at `0x80516000` and go down 7 rows until you find `0x80516070` then go to the right 4 bytes! ![](assets/images/Pasted%20image%2020231208075830.png)

The hex outlined in red shows the first 4 bytes (word) at address `0x80516074` therefore you can state that the word at address `0x80516074` is `0x38A00000`

# Chapter 4: Basic Registers
In modern CPU have thousands of registers but we don’t have to worry about most of them. 

Registers are spit into three groups 
- General (GPRs)
- Float (FPRs)
- Special (SPRs)

The guide here follows the ARM Cortex-A57 CPU which uses ARMv8 AArch64 assembly language. 

The Cortex-A57 has 31GPRs `r0` to `r30`  each register is 64 bits wide so they fit 2 words each. 

Two of the GPRs have alternate names
- `r29` being the **frame pointer FP**
- `r30` being the **link register LR**

Two special registers to also mention are 
- **program counter PC**
  - read only register keeps track of what instruction the CPU is currently executing 
- **Stack Pointer SP**
  - SP is used in conjunction with **LR** for subroutine use 


# Chapter 5: Assembler Installation & Quick Overview
Some of the tools used in the tutorial are: 

- **aarch64-linux-gnu-as** (The actual Assembler, what we use to make an object file out of a source text file written in ARMv8 Assembly)
- **aarch64-linux-gnu-ld** (Called the Linker. In the most basic terms, it creates an executable file out of an object file)
- **aarch64-linux-gnu-objdump** (What we use to see the Assembly Instructions contained within an Object file)


# Chapter 6: Instruction Format
The GRPs have two different modes, **Extended** and **Non-Extended** 

- **Extended** 
	- indicates that the whole 64 bits of the register will be used. 
	- prefixing the register with **x** will denote that the **Extended** mode is to be used I.e. x22
- **Non-Extended**
	- Only utilize the lower (right side) bits of the register 
	- Prefixing the register with **d** will denote that **Non-Extended** mode is to be used I.e. w11

## Register Formats
![](assets/images/Pasted%20image%2020240108134518.png)

The value type `immediate` is basically a constant value that is numercal and is not represented by what's in the Register. i.e. `mov d0, #1`

When dealing with **negative signed numbers** you must have the first bit of the immediate value by 1 and you must also have a condition branch set which is covered in chapter 10.
![](assets/images/Pasted%20image%2020240108140053.png)

## ARMv8 vs AArch64
`AArch74` is a specific instruction set within the entire `ARMv8` architecture. It is the standard instruction set for `ARMv8`. `ARMv8` does have two additional modes it can operate in, `AArch32/ARM32` or `Thumb32` for further compatability.
![](assets/images/Pasted%20image%2020240108141139.png)

# Chapter 7: Basic Instructions 
![](assets/images/Pasted%20image%2020240108190909.png)
When looking at the registers in gdb keep in mind that the decimal table (far right) will display the decimal in **64-bit signed decimal**. This cannot be changed it is a limitation of gdb 

Some assemblers like the gnu assembler does not require immediate values to be prefixed with `#` but it is good practice todo so as that is the official way to do it. 

# Chapter 8: Writing Full Values to Registers
It is a common problem with new users to write invalid number ranges into a GRP. The error is called **Invalid Immediate Value**. There are two techniques that this chapter is going to teach us to get around it.
1. **Literal Pools**
2. **Using "move" type instructions**

## Literal Pools
Literal Pool is basically an Assembler trick that allows us to write in values to a register without using a **mov-type** instruction

To signal to the assembler that the instruction is using a pool literal you use the **=** symbol when assigning with a literal as such:
```arm-asm
ldr w10, =0x5FFF0FFF
```

## Using "move" type instructions 









---
# Low Level Learning Video
- The army architecture has two operating modes: 
	- ARM - 4-byte instructions
	- THUMB - 2-byte instructions 
- ARM is byte addressable meaning that you can request any size memory unlike `mips` which requires you to request in 4-byte chunks

- ARM Instructions take the form of
```
<operator> <dst>, <src>
<operator> <dst>, <immediate> # Immediate being a const
<operator> <dst>, [address]
```

- Basic ARMv8 file
```arm-asm
.global _start # Make _start globally accesible needed to compile
section .text # Defines that this section is .text (code)

_start:

.section .data # defined that this section is .data
```



---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`

[AArch64/ARM64](https://mariokartwii.com/armv8/)
[Armv8 Video](https://www.youtube.com/watch?v=FV6P5eRmMh8&t=16s)
