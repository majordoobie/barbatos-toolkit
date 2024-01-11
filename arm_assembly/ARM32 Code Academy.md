---
parent file:
  - "[[Root]]"
related: 
creation data: 2024-01-10, 22:37
tags:
---
# Basics
## Registers 
Some of the special registers are 
- r7 — used to set up a system call with `svc`
- sp — identifies the current location in the stack 
- ir — the “return” address for a function 
- pc — address of the next instruction to execute 
- cpsr — special register to store information about the program like subtracting and getting a negative number. There is a flag in memory that denotes if the result is negative or not 
- spsr — 


## Structure 
- label is synonymous with **function** in higher level languages 
- `.global` allows external entities to see the labels of the program. By setting `.global _start` allows the linker to know where the start of the program is 
- when wanting to kill a program you want to perform an interrupt. This is done with the `swi` op code 
```armasm 
.global _start

_start:
	mov r7, #1
	swi 0

```


# Addressing 
Immediate addressing involves moving from immediate value into a register
```armasm
.global _start

_start:
	mov r0, #1
```

Registered direct addressing is when we move data from one register into another
```armasm 
.global _start

_start:
	mov r1, r0
```

Finally we have direct addressing. This involves moving data from the stack into a register. But first we need to figure out how to get data into the stack. 
```armasm
.global _start
	ldr r0, =list

_start:
	ldr r0, =list

.data // signifies the data section
list:
	.word 4,3,-1,0
```
**.data** 
- indicates the start of the data section. 
- Data in here is stored in the stack 
**list:**
- just like the function labels these labels are like variables
**.word** 
- the data type of the label. In this case each element in our array is a **.word** or 32 bits
**ldr** 
- the `ldr` instruction loads the address of the label into the register. The location of a label has to be prefixed with `=`
- This is known as direct addressing 
- Just like in c, the address of the array is also the first element. So really, the destination register contains the address if the first element 

---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 
[freeCodeCamp](https://youtu.be/gfmRrPjnEw4?si=oY9XhUFZX8pPmshU)