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
	svc 0

```


# Addressing 
Immediate addressing involves moving from immediate value into a register
```armasm
.global _start

_start:
	mov r0, #1
	mov r7, #1
	svc 0
```

Registered direct addressing is when we move data from one register into another
```armasm 
.global _start

_start:
	mov r1, r0
	mov r7, #1
	svc 0
```

Finally we have direct addressing. This involves moving data from the stack into a register. But first we need to figure out how to get data into the stack. 
```armasm
.global _start
	ldr r0, =list
	ldr r1, [r0]
	ldr r2, [r0, #4] //indirct addressing
	ldr r3, [r0, #4]! // pre addressing
	ldr r4, [r0], #4 // pre addressing 
	mov r7, #1
	svc 0

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

**ldr r0, =list** 
- the `ldr` instruction loads the address of the label into the register. The location of a label has to be prefixed with `=`
- This is known as **direct addressing**
- Just like in c, the address of the array is also the first element. So really, the destination register contains the address if the first element 

**ldr r1, [r0]**
- this syntax known as **register indirect addressing** is how you fetch the data of an address. 
- The square bracket does the fetching just like the star operator in C 

**ldr r2, [r0, #4]**
- fetches the next value by incrementing the start address by 4 bytes. This works because each data type in the array is a word or 4 bytes long 

**ldr r3, [r0, #4]!**
- the exclamation at the end performs a **pre-increment**
- this will change the address before doing a indirect addressing. The difference is that the **r0** will maintain the changed address after the addressing 

**ldr r4, [r0], #4**
- this is **post-increment**  think as the brackets doing the addressing **AND THEN** the address is moved forward. Just like pre, the address is permanently changed in r0


# Arithmetic and CSPR flags 
Some instructions automatically set flags within the **CSPR** register. This arithmetic section is an easy way to interact with the **CSPR** 

## Example of Arithmetic
```armasm
.global _start

_start:
	mov r0, #5
	mov r1, #7
	add r2, r0, r1 // r2 = r0 + r1
	mul r2, r0, r1 // r2 = r0 * r1
	sub r2, r0, r1 // r2 = r0 - r1
```

## The CSPR Register
### CSPR Register Negative
Now, say we subtracted **5 - 7** you would get **-2**. In the **r2** register you would get the hex value of **0xFFFFFFFE** . If signed this is **-2** but if unsigned this would be **4294967294**. So how do we know which one it is? 

The register will create the flags of **NZCVI** to represent the different flags of the operation results. The **N** in the series of flags stands for **negative**. So, when we do some kind of arithmetic we can use this value to tell if the result was either a negative decimal or a positive decimal.

In order for this register to be set with the appropriate flags, you have to use instructions that sets it. So for subtraction, you would use **SUBS**. The reason we have to use a seperate instruction is because there is an additional instruction needed to load the data into the **CSPR** register which adds additional overhead.

You should use **SUBS** when you know you are doing to be dealing with negative numbers or you don't know what the values are going to be like if loading it from some memory locations and not know what they are going to be.

```asmarm
.global _star

_start:
	mov r0, #5
	mov r1, #7
	subs r2, r0, r1
	

```


### CSPR Register Carry





---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 
[freeCodeCamp](https://youtu.be/gfmRrPjnEw4?si=oY9XhUFZX8pPmshU)