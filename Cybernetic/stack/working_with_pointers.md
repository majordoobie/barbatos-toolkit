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

### Working with pointers
- If you were to increment a pointer, say by 1, it would increment one `value` based on the data type. For integers, this is four bytes. So incrementing by 1 increments by 4 bytes.
```c++
int main()
{
	int a = 10;
	int *p = &a;
	
	printf(p)      // 2000
	printf(p + 1)  // 2004
	printf("Size of integer is %lu bytes\n", sizeof(int));
}
```

### Pointer types
- Pointers are strong types just like a normal variable
- int* is used for int and char* is used for char
- If you were to create a variable of type int then then cast the results to a char variable it would truncate the values

```c
int a = 1025;
int *p = &a;
char *p0 = (char*)p;  // p0 becomes 1
```
```
// a is an int so it is saved in a 4 byte continues address

00000000 00000000 00000100 00000001

// When *p0 = (char*)p; only the first byte is saved to p0 since it's a char type which only has one byte

00000001

```

---
## Metadata
- `tags`: 
- `Title`: working_with_pointers
- `Created`: [[20210227]] 16:53

==References==
- [Pointer Series](https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_)