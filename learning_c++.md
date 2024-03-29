---
parent file:
  - "[[../Zettelkasten_old/Published]]"
related: 
creation data: 2020-12-05, 07:10
tags:
  - "#guides"
  - "#code"
---

# Learning C++
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
![](Pasted%20image%2020210227172720.png)

- Pointers are variables that store the address of another variable
![](Pasted%20image%2020210227174743.png)
![](Pasted%20image%2020210227181349.png)

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

- void pointers are generic pointers that don't align with a particular type
- Void pointers can only store the address of something you cannot dereference it to get the value because the data type in the pointer is not known. 
```c++
int main()
{
	int a = 1025;
	int *p = &a;
	void *p0 = p;
}
```

### pointers as function arguments
- When you run your program the application in memory creates four parts, the code portion, the static/global portion, the stack portion and the heap portion
- Each scope of your program is saved in a record called the stack frame. All variables for that scope are saved in that frame
![](Pasted%20image%2020210227213201.png)


## Caleb's playlist
### Structs vs Classes
- structs and classes are similar types in C++
- A big difference is that in C++ structs are used for data only or PODS ==Plain Old Data Structure==
- Your normally want to avoid putting methods in structs with C++

### Classes and Objects
- With C++ when you want to create a new object you don't use the `new` keyword or call the class and assign it to a variable like you do with python instead you do this fucked up way:
```C++
User user;    // yup that's it

User user(int arg1, string var2); // or with params
```

- If you do not provide a default constructor, there will be one present anyways. It just takes no variables.
- You can overload the constructor with different signatures
- If you do not want a default constructor, then you would only add the custom constructor and omit adding the default constructor 
- Since a default constructor exits, you do not have to write a constructor at all and it will still work
```c++
class A
{
	// notice that no constructor is written but still called
	public:
		void print() {}
}

int main()
{
	A a;
	a.print();
	return 0
}
```

- To be able to enable overloading of constructors, a empty constructor must be present otherwise it will throw an error
```c++
class A
{
	public:
		A() {}
		A(int id) 
		{
			this->id=id;	
		}
}
```

![](Pasted%20image%2020210228022424.png)

```
<program> → <exp> , <assigns> ;
<exp> → ( <operand> <op> <operand> ) |  ( <operand> : <operand> '?' <operand> ) | ( <operand> '!' )
<operand> → <literal> | <variable> | <exp> 
<assigns> → <assigns> , <assign> | <assign>
<assign> → <variable> = <literal>


<op>		'+' | '-' | '*' | '/' | '>' | '<' | '=' | '&' | '|'
<variable>	\[a-zA-Z\]\[a-zA-Z0-9\]\*
<literal>	\[0-9\]+
```
---

### Reading and Writing with C++
- To write to files you need `<fstream>`
- `std::ofstream` is the name of the class to create an instance of the file object
- To actually get a file handle you pass in the file object
```c++
#include <iostream>
#include <fstream>

int main()
{
	std::ofstream file("file_name");
	
	if (!(file.is_open()))
	{
		std::cout << "FUCKKK" << endl;	
	}	
	
	std::vector<std::string> names;
	names.push_back("Jason");
	names.push_back("Corey");
	
	for(std::string name : names )
	{
		file << name << std::endl;	
	}
	
	file.close();
	return 0;
}
```

- Reading from a file uses the `ifstream`
```C++
int main()
{
	std::ifstream file("file_name");
	std::vector<std::string> names;
	
	std::string input;
	while(file >> input)
	{	
		names.push_back(input);			
	}	
	
	for(std::string name: names)
	{
		std::cout << name << std::endl;	
	}
}
```

## Cherno
### Pre processor
- the include statemen will literally paste data from where ever its coming from
- the `#if` and `#endif` will only execute code between the two lines if the condition is true
- if you output your code into assembly you can start to see when you are doing dumb shit 
- When allowing the compiler to `optomie` it will literally try to improve your code to make the assembly perform its task with less instructions. it will even remove code if it deems it unnecessary
- `constant folding` is resolving constants at compile time insteaf of runtime  

### Linking
- linker links all your files together to make one application and registers the entrypoint
- Compiling will not link but if you build it will compile AND link
- Error codes that start with `C` have to do with the compiler such as syntax and sementic errors
- Error codes that start with `L` have to do eith the linker such as not having a define entrypoint
- Entrypoints by default is the main function but you can overwrite that
- If using static on a function you atr saying that the function will only be available in this execution unit no other unit can access it 

### Variables
- The real difference between data tyes is how many bytes they are 
- with four bytes of sign int you can store between -2b to 2b
- to get your your bits worth you can request an unsign int
- you need to append an f after a float to declare a float
- you can use `sizeof(obj)` to get yhr size of whatever you are passing in

### Header Files
- cpp files are the compilation init 
- header files are used for declarations and more
- declarations just says that a function exists it is not a definition
- without a header file you would need to declare the signature of every function you want access to in each execution unit
- by using a headerfile that has your declarations and using the `#include "header.h"` you are just pasting the declarations in the header into each execution unit
- `#progma once` is a header guard that prevents duplicating header files that can be caused by chaining includes in a complicated project 
- the traditional header guard is to use the following 

```c++
#ifdef _SOME_VAR
#define _SOME_VAR

void signature();
void signatures();

#endif
```
- which means if the `_SOME_VAR` is not defined then allow the include. When the header is about to get included again it will see that `_SOME_VAR` is already defined and it will prevent the declarations from getting re-included

- distinctions between includes
```
#include "my_header.h" 
#include <c_standard_lib.h>
#include <cpp_standard_lib>
```

## Local Static in C++ 
- When you have a function with a static variable it will be initialized when it is first called. After that, it will no longer be re-initialized even if the variable is local to that function
- The benifit of this is that only the function has access to this local variable. Because access is still limited to the scope by the lifetime is the lifetime of the program. So it will act like a global as long as the program is access it via the function with the static variable

## Enums
- Defines a set of values with integers
- It names values or states so that the code is more readible must behind it all it's just an intiger
- By default enums will get assign an interger automatically starting from one
- You can also manually assign them with a equal sign
```c++
enum Example
{
  A = 20, B = 1, C = 30
};

int main()
{
  if (20 == A)
  {
    // do something
  }
}
```
- Since enum are integers by default, it would be wise to use a `char` when possible to use one byte instead of four
```C++
enum Example : char
{
  A = 20,
  B = 200,
  C = 0
}
```
- When you assign a variable to a enum, you can set the variables Type since it is just a integer. But if you want to constraint it to the choices you want to set the variable type to the Enum name
```c++
enum Speed : char
{
  Slow = 10,
  Fast = 30
};

int main()
{
  int currentSpeed = Slow;   // Acceptable
  Speed maxSpeed = Fast      // prefered
}
```

## Constructor
- If for some reason you don't want people to instanciate your class you can hide your constructor in the private section which will prevent instanciation 
- Additionally you can set the construtor to `delete`
```c++
class Excample
{
public:
  Example() = delete;
};
```

## Destructors
- Destructor always runs when a object is destroyed
- This is the best place to close handles or release memory

## Inheritance
- 

## Metadata
- `tags`: 
- `Title`: working_with_pointers
- `Created`: [[20210227]] 16:53

==References==

- [Cherno](https://youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)

- [Pointer Series](https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_)
- [Classes in C++](https://www.youtube.com/watch?v=ABRP_5RYhqU)
- [Structs vs Class](https://www.youtube.com/watch?v=vJ9ezXY7efw&list=PL_c9BZzLwBRJVJsIfe97ey45V4LP_HXiG&index=84)
