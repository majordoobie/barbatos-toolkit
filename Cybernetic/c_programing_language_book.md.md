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