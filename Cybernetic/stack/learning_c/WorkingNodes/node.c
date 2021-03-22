#include <stdio.h>
#include <stdlib.h>
#include "node.h"

Node make_Node(int value)
{
    Node temp = {value};
    printf("%p\n", &temp);
    return temp;
}

Node *make_Node_prt(int value)
{
    Node *temp = (Node*)malloc(sizeof(Node));
    temp->value = value;
    printf("%p\n", temp);
    
    return temp;
}