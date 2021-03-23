#include <stdio.h>
#include <stdlib.h>
#include "node.h"

Node *make_node(int value, Node *head_node)
{
    Node *new_node = (Node*)malloc(sizeof(Node));
    new_node->value = value;
    new_node->left = head_node;

    if (head_node != NULL)
    {
        head_node->right = new_node;
    }

    return new_node;
}

void to_string(Node *node)
{
    printf("Node: %p has a value of %d\n", node, node->value);
}

void iter_nodes(Node *head_node)
{
    Node *current_node = head_node;
    while (current_node != NULL)
    {
        to_string(current_node);
        current_node = current_node->right;
    }
}
Node *get_last_node(Node *head_node)
{
    Node *current_node = head_node;
    Node *previous_node = head_node;
    while (current_node != NULL)
    {
        previous_node = current_node;
        current_node = current_node->right;
    }
    to_string(previous_node);
    return previous_node;
}