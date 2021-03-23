#include <stdio.h>
#include <stdlib.h>
#include "node.h"

/*
 * Function:    make_node
 * -----------------------
 * Constructor for making new nodes. It takes in head node
 */
Node_var *make_node(int value, Node_var *head_node)
{
    // create the new node
    Node_var *new_node = (Node_var*)malloc(sizeof(Node_var));
    new_node->value = value;
    new_node->right = NULL;

    if (head_node != NULL)
    {
        //  get last node in the chain
        Node_var *previous_node = get_last_node(head_node);
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
void to_string(Node_var *node)
{
    printf("Node_var: %p has a value of %d\n", node, node->value);
}

void iter_nodes(Node_var *head_node)
{
    Node_var *current_node = head_node;
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
Node_var *get_last_node(Node_var *head_node)
{
    Node_var *current_node = head_node;
    Node_var *last_node = head_node;
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
void free_nodes(Node_var *head_node)
{
    Node_var *last_node = get_last_node(head_node);
    Node_var *current_node = last_node;
    while (current_node != NULL)
    {
        current_node = current_node->left;
        printf("Freeing node at: %p\n", last_node);
        free(last_node);
        last_node = current_node;
    }
}