#include <stdio.h>
#include <stdlib.h>
#include "node.h"

Node *make_node(int value, Node *right_node)
{
    Node *temp = (Node*)malloc(sizeof(Node));
    temp->value = value;
    temp->right = right_node;

    return temp;
}

void to_string(Node *node)
{
    printf("Node: %p has a value of %d\n", node, node->value);
}
