# Memory
- `<stdlib.h>` provides four functions to allocation memory. They are
	- malloc
	- calloc
	- free
	- realloc
## malloc
> **“malloc”** or **“memory allocation”** method in C is used to dynamically allocate a single large block of memory with the specified size. It returns a pointer of type void which can be cast into a pointer of any form. It initializes each block with default garbage value.
```c
ptr = (cast-type*) malloc(byte-size)
 if (ptr == NULL) { 
        printf("Memory not allocated.\n"); 
        exit(0); 
    } 

```

## Calloc
> “calloc” or “contiguous allocation” method in C is used to dynamically allocate the specified number of blocks of memory of the specified type. It initializes each block with a default value ‘0’.
```c
ptr = (cast-type*)calloc(n, element-size);
```

## free
> “free” method in C is used to dynamically de-allocate the memory. The memory allocated using functions malloc() and calloc() is not de-allocated on their own. Hence the free() method is used, whenever the dynamic memory allocation takes place. It helps to reduce wastage of memory by freeing it.


## Resources
[Memory Allocation](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/)