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
Typical memory outputs are dumped in hex with 16 bytes across. Since they are 16 bytes across, each row increments by 16 bytes or `0x10` making it easier to visualize the increments. So, if you want to find address `0x80516074`, you start from the stop at `0x80516000` and go down 7 rows until you find `0x80516070` then go to the right 4 bytes! ![[Pasted image 20231208075423.png]]





---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`

[AArch64/ARM64](https://mariokartwii.com/armv8/)
