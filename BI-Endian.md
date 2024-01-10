---
parent file:
  - "[[Published]]"
related:
  - "[[arm_assembly/Introduction to Arm Assembly Basics]]"
creation data: 2023-12-07, 14:42
tags:
  - "#guides"
  - "#research"
---
# BI-Endian
Bi-Endian is the ability for a processor to be able to read in both big-endian and little-endian. The switch affects how memory is accessed in data-fetches, data-stores or both. The feature can sometimes improve performance and minimize the complexity of programs.

When hardware is said to be bi-endian, such as ARMv3+, it denotes that the hardware itself supports the ability to switch the endianness that it supports.

It is important to note that the implementation may differ between hardware. For instance, some hardware may support switching endianness but only on the data store/fetched while the instructions are fixed endian. [^Wiki]

# Endianness

Endianness is the byte-order in which each byte of an object is stored in memory. Little-endian (LE) like x86 is stored where the **least-significant-byte** is stored at the lowest address. Addresses typically grow from bottom to top, were the bottom is the lowest address. Therefore, in little-endian the bytes flow in the oder from bottom to top.

Big-endian on the other hand is the other way around and it is the preferred byte-order of networking data
![](assets/images/Pasted%20image%2020231208080046.png)


---
# Resources
 `[Example](Link)`
 `[^Example]: Link    || [^Example]`

[^Wiki]: https://en.wikipedia.org/wiki/Endianness

 
