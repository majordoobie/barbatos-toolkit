#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "node.h"


//doxygen

/*
 * Function:    make_node
 * -----------------------
 * Constructor for making new nodes. It takes in head node
 */

struct Node
{
    int value;
    struct Node_var *left;
    struct Node_var *right;
};

Node_t *make_node(int value, Node_t *head_node)
{
    // create the new node
    // All the data in the memory is set to Ox0
    Node_t *new_node = (Node_t*)calloc(1, sizeof(Node_t));

    struct Node something_node = { 0 };

    new_node->value = value;
    new_node->right = NULL;

    if (head_node != NULL)
    {
        //  get last node in the chain
        Node_t *previous_node = get_last_node(head_node);
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
void to_string(Node_t *node)
{
    printf("Node_t: %p has a value of %d\n", node, node->value);
}

void iter_nodes(Node_t *head_node)
{
    Node_t *current_node = head_node;
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
Node_t *get_last_node(Node_t *head_node)
{
    Node_t *current_node = head_node;
    Node_t *last_node = head_node;
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
void free_nodes(Node_t *head_node)
{
    Node_t *last_node = get_last_node(head_node);
    Node_t *current_node = last_node;
    while (current_node != NULL)
    {
        current_node = current_node->left;
        printf("Freeing node at: %p\n", last_node);
        free(last_node);
        last_node = current_node;
    }
}