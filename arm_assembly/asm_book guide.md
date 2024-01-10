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



---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 
[asm_book](https://github.com/pkivolowitz/asm_book/tree/main)

[^system_call]: https://github.com/pkivolowitz/asm_book/blob/main/more/system_calls/README.md

[^system_call_num]: https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#arm64-64_bit
