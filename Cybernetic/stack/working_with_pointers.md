# working_with_pointers
## Working with pointer playlist
### Introduction to pointers
- Each byte of RAM memory has an address starting from 0
- When you create a variable, the compiler will allocate some memory for that variable based on the data type. For integers this is usually 4 bytes
- There is a lookup table in a program that keeps a mapping of the variables initialized so if we create a variable a:
```c
int a;
```
- Then the compiler will allocate 4 bytes for this variable and the `lookup tabled` will list that variable a is an int and it's located in memory address x
- When a variable, such as `a`, is initialized with a integer, say 5, the compiler will look in the lookup table and see that the variable `a` starts at memory address x then puts the binary 5 in that space
![](attachments/Pasted%20image%2020210227172720.png)

- Pointers are variables that store the address of another variable
![](attachments/Pasted%20image%2020210227174743.png)
![](attachments/Pasted%20image%2020210227181349.png)



---
## Metadata
- `tags`: 
- `Title`: working_with_pointers
- `Created`: [[20210227]] 16:53

==References==
- [Pointer Series](https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_)