---
parent file:
  - "[[Root]]"
related: 
creation data: 2024-01-10, 16:14
tags:
---
# Under the hood: System Calls
When making system calls, the kernel performs the call within its own private region of memory. Our programs run in "userland". The technical name for userland on the ARM64 processor is EL0 (Exception Level 0). [^system_call]

We can operate within the kernel's space only through carefully controlled mechanisms - such as system calls. The technical name for where the kernel (or system) generally operates is called EL1.

## Making System Calls
In order to make a system call there are 3 things that need to be met
1. The parameters for the system call must be assigned to the appropriate register [^system_call_num]
2. The **w8** register must be populated with the system call that we want to make [^system_call_num]
3. The **svc** instruction is executed which elevates the program from EL0 to EL1 to perform the call

Linux supports many system calls but depending on the platform the number for the system call has changed. This link shows a whole list of the system calls per architecture: [link](https://gpages.juszkiewicz.com.pl/syscalls-table/syscalls.html)

## Using compilers to automation
![](assets/images/Pasted%20image%2020240110163718.png)

Instead of manually assembling and linking we can use gcc/clang to automate the process for us assuming that we want to link the **crt**

# Hello World Example
The book starts with comparing a C and Assembly version of a helloworld program

```c
#include <stdio.h>

int main(int argc, char * argv[]) {
	top:
		if (*argv == NULL)
			goto bottom;
		puts(*(argv++));
		goto top;

	bottom:
		return 0;
}
```

The it compares it to the assembly of it which looks like this
```armasm
	// The .global insructs the assembler to make main visible 
	// to the linker. If compiling with crt, you will need a
	// main function/label by default
    .global main

// The label main only differs from top and bottom by it being the 
// only one that is visible to the linker because of the .global 
// directive above
main:
    stp     x21, x30, [sp, -16]!    // push onto stack
    mov     x21, x1                 // argc -> x0, argv -> x1
    
top:
    ldr     x0, [x21], 8            // argv++, old value in x0
    cbz     x0, bottom              // if *argv == NULL goto bottom
    bl      puts                    // puts(*argv)
    b       top                     // goto top
    
bottom:
    ldp     x21, x30, [sp], 16      // pop from stack
    mov     x0, xzr                 // return 0
    ret
    
    .end
```





---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 
[asm_book](https://github.com/pkivolowitz/asm_book/tree/main)
[List of System Calls by Arch](https://gpages.juszkiewicz.com.pl/syscalls-table/syscalls.html)

[^system_call]: https://github.com/pkivolowitz/asm_book/blob/main/more/system_calls/README.md

[^system_call_num]: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#arm64-64_bit
