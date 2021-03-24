#include <stdio.h>
#include "node.h"


int main(void)
{
    Node *null_node = NULL;
    Node *head_node = make_node(0, null_node);

    make_node(10, head_node);
    make_node(324, head_node);
    make_node(44, head_node);

    iter_nodes(head_node);


    // clean up and free nodes
    free_nodes(head_node);
    return 0;
}







// allocate memory for head
// insert Nodes with corresponding integer values one by one
