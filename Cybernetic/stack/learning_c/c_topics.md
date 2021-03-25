# headers containing different topics
## Memory allocation
- If using `malloc`, you need to use `memset` to initialize the data to be set to 0 that way you are not surprised when you see some crazy garbage. 

```c
Node_t *new_node = (Node_t*)malloc(sizeof(Node_t));
memset(new_node, 0, sizeof(Node_t));
```

- Alternatively you can use `calloc` which allocates the memory and initializes them to 0
```c
Node_t *new_node = (Node_t*)calloc(1, sizeof(Node_t));
```

## Structures with typedef
- Normally when you want to add your structure declaration to a header file you have to include the members inside the structure of the declaration preventing you from keeping the data private. What you can do is instead of using `typedef` and `struct` together to define the structure you can instead define your structure in your `.c` file then use the `typedef` for the structure in the header file

```c
// file.c
struct Node
{
    int value;
    struct Node_var *left;
    struct Node_var *right;
};


// file.h
typedef struct Node Node_t
```