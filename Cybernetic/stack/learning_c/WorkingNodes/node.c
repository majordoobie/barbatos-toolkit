#include <stdio.h>
#include <stdlib.h>
#include "node.h"

/*
 * Function:    make_node
 * -----------------------
 * Constructor for making new nodes. It takes in head node
 */
Node *make_node(int value, Node *head_node)
{
    // create the new node
    Node *new_node = (Node*)malloc(sizeof(Node));
    new_node->value = value;
    new_node->right = NULL;

    if (head_node != NULL)
    {
        //  get last node in the chain
        Node *previous_node = get_last_node(head_node);
        new_node->left = previous_node;
        previous_node->right = new_node;
    }
    else
    {
        // Should only occur during init
        new_node->left = NULL;
    }

    return new_node;
}

/*
 * Function:     to_string
 * ------------------------
 * Prints the current node
 */
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
/*
 * Function:        get_last_node
 * -------------------------------
 * Gets the last node by iterating to the right
 */
Node *get_last_node(Node *head_node)
{
    Node *current_node = head_node;
    Node *last_node = head_node;
    while (current_node != NULL)
    {
        last_node = current_node;
        current_node = current_node->right;
    }
    return last_node;
}

/*
 * Function:    free_nodes
 * ------------------------
 * Iterates over the nodes to free them
 */
void free_nodes(Node *head_node)
{
    Node *last_node = get_last_node(head_node);
    Node *current_node = last_node;
    while (current_node != NULL)
    {
        current_node = current_node->left;
        printf("Freeing node at: %p\n", last_node);
        free(last_node);
        last_node = current_node;
    }
}