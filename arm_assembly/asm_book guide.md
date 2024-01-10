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




---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`
 
[asm_book](https://github.com/pkivolowitz/asm_book/tree/main)

[^system_call]: https://github.com/pkivolowitz/asm_book/blob/main/more/system_calls/README.md