#include <stdio.h>
#include <stdlib.h>
#include "node.h"

Node make_node(int value)
{
    Node temp = {value};
    printf("Printing from make_node: %p\t\n", &temp);
    return temp;
}

Node *make_node_ptr(int value, Node *right_node)
{
    Node *temp = (Node*)malloc(sizeof(Node));
    temp->value = value;
    temp->right = right_node;
    printf("Printing from make_node_ptr: %p\t\n", temp);

    return temp;
}
