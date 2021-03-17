# C Programming Language
By: Brian W. Kernighan and Dennis M. Ritchie 
The book is also known as K&R
## Introduction
- ==Symbolic Constants== are a type of variable that is not declared and is used just like a constant is. It's meant to give "meaning" to variables 
```c
#define UPPER 100 /*You can add a comment here too */

int main()
{
	int start = UPPER;
}
```

- Input and output is dealt in ==text streams== which are lines of text that are `\n` separated. Libraries must adhere to this standard when dealing with input and output
- When reading `char` from `getchar()` function; most often you will use the `EOF` built in which is larger than a byte since it's a integer. So if you are looping through `getchar()` it is wise to use an integer to hold the value of `EOF` even though `getchar()` grabs one byte characters
- The `EOF` is a ==symbolic constant== from the `<stdio.h>` library 
- When writing a character in single quotes represents an integer value that is that is equal to the machines character set for that character
- In the box I was asked to reverse a string this is what I cameup with
```C
char* reverse_string(char array[])
{
    int array_length = sizeof(array) / sizeof(char);
    int new_array_index = 0;
    char* reverse = (char*)malloc(array_length * sizeof(char));
    
    for (int old_array_index = array_lengt - 1; old_array_index >= 0; --old_array_index)
    {
    	reverse[new_array_index] = array[old_array_index];
	++new_array_index;
    }
    return reverse
}
```

## Chapter 2 Types, Operators, Expressions
- The first 31 characters of an intername are significant 
- Ints can be modified with `short` or `long`; `short` is at least 16 bits and `long` is at least 32 bits
- `unsigned` is always 0 or positive
- `<limits.h>` and `<float.h>` provide limits for precesion used in `float` `doubld` `long double`
- To use `#include <math.h>` you need to link the file with `-lm` so `gcc -Wall -std=c99 get_ranges.c -lm -o out/get_ranges.o`
- If you want to do a bit shift like this
```c
unsigned long binary = 1 << bits;
```
- The 1 is a int constant if you want a long you have to specify it with an L
- The character constant `\0` is often used as a NULL but it's value is just 0
- A string constant (double quotes) is an array of characters
- 'A' does not equal "A"
	- 'A' is an integer used to represent a character
	- "A" is an array with one character 'A' and null at the end `\0`

- Enums are supported in C
```c
enum months { JAN = 1, FEB, MAR, APR, MAY, JUN,  
 			  JUL, AUG, SEP, OCT, NOV, DEC };
```

- A warning can be produced by the compiler when automatic type casting is done like adding a long into a integer where information can be lost
- If non character data is to be stored in a `char` make sure to specify `signed/unsigned` 
![](attachments/Pasted%20image%2020210317153534.png)


## Chapter 3 Control Flow
- semicolons are used to terminate statements
- curly braces are used to group statements or `block`

## Chapter 4 Functions and Program Structure