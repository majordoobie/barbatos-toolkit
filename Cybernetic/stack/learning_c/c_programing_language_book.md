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
- When compiling multiple files you can add all the source files in the same command:
`cc main.c secondary.c third.c`
- If there is an error with a file, like C when compiling, you do not need to compile the other objects. 
`cc main.c secondary.o third.o`
- It's often  better to use a single header file that has all the declarations for all the source codes that need it
- `register` declaration tells the compiler to save the variable in a register if the variable will be used a lot. The compiler is able to ignore this though 
- `external` and `static` variables are automatically initialized to 0
- A character array is a special array that takes a unique syntax
```c
char pattern[] = "ould";
// equals the following
char pattern[] = { ′o′, ′u′, ′l′, ′d′, ′\0′ };
```

### Preprocessor
- Preprocessor are things that occur before actual compilation
- The most used features are `#define` and `#include`
- The `#include` statement gets replaced with the contents of whatever file is being included like a "copy and paste"
- Header guards is also supported in C using the `#if`
```c
#if !define(HDR)
#define HDR
// code
#endif
```
- A cool way to use this as found in the book is:
```c
#if SYSTEM == SYSV

    #define HDR "sysv.h"

#elif SYSTEM == BSD

    #define HDR "bsd.h"

#elif SYSTEM == MSDOS

    #define HDR "msdos.h"

#else

    #define HDR "default.h"

#endif

#include HDR
```

## Chapter 5: Pointers and Arrays
- With C99 you an use `void* ptr` as a generic pointer
- Pointers are often 2 or 4 bytes that hold the address of something
- To get the address of an object you use the `&` operator. The operator only works against objects in memory
- The `*` is a dereference operator; when used on a pointer it gets the object at the address

```c
int x = 1, y = 2, z[10];

int *ip;         /* ip is a pointer to int */



ip = &x;         /* ip now points to x */

y = *ip;         /* y is now 1 */

*ip = 0;         /* x is now 0 */

ip = &z[0];      /* ip now points to z[0] */
```
- In c pointers and arrays are practically the same thing and work exactly the same way which means that subscribing also works with pointers
- If an array were to be created and I set the pointer to the first element then I can subscribe the pointer to the next element in the array just like using the array

```c
int array[10]
int *ptr = &array[0];

// You can move up the array chain with
*(ptr+1); // equivalent to array[1];

```

- When using the syntax `array[index]` C will actually convert that to say `*(array + index)`
- When passing a array name to a function, what is passed is the location of the first element of the array
- You can subscribe a char array by looking for `\0`! if passing it to a function since the function is only getting the first element
```c
int string_length(char *string)
{
	int length;
	for (length=0; *string != '\0'; *s++)
		{
			length++;
		}
	return length;
}
```

- String constants are written with double quotes and their length is +1 their contents because of the termination with `\0`
```c
char amessage[] = "now is the time";   /* an array */

char *pmessage = "now is the time";    /* a pointer */
```

- To copy a string to another variable you have to manually iterate over the array. I want to point out that the result of an assignment is the left most result
```c
void strcpy(char *s, char *t)

{
    int i;
    i = 0;

    while ((s[i] = t[i]) != ′\0′) // Result of = is s[i]
        i++;
}
```
or
```c
   void strcpy(char *s, char *t)
   {
       while ((*s++ = *t++) != ′\0′)
           ;
   }
 ```
 
 - When storing an array of strings, remember that this is a array of arrays. But, even though you can legal use `int *b[10]` to make the same thing as `int a[10][20]` the latter sets aside 200 integers while the former doesn't initialize the inner array so the latter is the right way to do it
 - Additionally, using a array to store a strings is just an array of arrays `char *name[] = {"Monday", "Tuesday"};`
 ![](attachments/Pasted%20image%2020210319085447.png)
 
 ### Command Line arguments
 - When passing arguments to main from the command line there are two variables used `argc` which takes a count of the arguments and `argv` which is a array of arguments 
 - Just like python, the first item in the array is the name of the program. Therefore, argc will always be at least 1
 
 
 ## Chapter 6: Structures
 - Attributes in structures are called members
 - When creating a structure you can instantiate a object by passing in the list of expected variables
 
 ```c
 struct point
 {
 	int x;
	int y;
 }
 
 struct point declared;
 struct point initialized = {100, 300};
 ```
 - Of course, it is more efficient to pass a pointer to a function rather than passing the values of the structure to the function which could have a ton of data
 ```c
struct point origin, *pp;
pp = &origin;

printf("origin is (%d,%d)\n", (*pp).x, (*pp).y);
 ```
 - Or you could use the short hand of `->` 
 ```c
 struct Node first = {100, 200};
 struct Node *pointer = &first;
 
 printf("First: %d\nSecond:%d\n\n", first.first, first.second);
 printf("First: %d\nSecond:%d\n\n", (*pointer).first, (*pointer).second);
 printf("First: %d\nSecond:%d\n\n", pointer->first, pointer->second);
 ```
 - When creating a array of structs you have the option of using a short cut that I think looks ugly
 
 ```c
 struct key
 {
 	int val;
	int val;
 } array_key[MAX];
 
 // vs
 struct key
 {
 	int val;
	int val;
 };
 struct key array_key[MAX];
 
 ```
 
 ### Sizeof
 - size of produces a unsigned integer representing the size of the object in bytes known as `size_t` this is defined in `stddef.h`

### Typedef
- Typedef allow you to create a new data type
- For example using it to create a String data type
```c
typedef char *String;
// equals
String name = "Jay";
char *name = "Jay";
```

- Or they can be used for structures too
```c
typedef struct tnode *Treeptr;

typedef struct tnode {   /* the tree node: */
    char *word;              /* points to the text */
    int count;               /* number of occurrences */
    Treeptr left;            /* left child */
    Treeptr right;           /* right child */

} Treenode;

```

- This creates two new types, Treenode and Treeptr. this just makes it easier to read


## Chapter 7: Input and Output
- The syntax `<` and `>` can be used to pull and push from a stream

> When a C program is started, the operating system environment is responsible for opening three files and providing file pointers for them. These files are the standard input, the standard output, and the standard error; the corresponding file pointers are called stdin, stdout, and stderr, and are declared in <stdio.h>. Normally stdin is connected to the keyboard and stdout and stderr are connected to the screen, but stdin and stdout may be redirected to files or pipes as described in 
### String functions
![](attachments/Pasted%20image%2020210319130727.png)


## Chapter 8: Unix Interface
- file descriptor is analogous to file pointer used in unix or file handle used in windows
- All information about the open file is handled by the system and programs interact with the resource using the pointer



