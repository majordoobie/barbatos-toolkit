#include <stdio.h>
#include "node.h"


int main(void)
{
    printf("Are we hitting main?");
    Node *null_node = NULL;
    Node *head_node = make_node(0, null_node);

    to_string(head_node);
    return 0;
}







// allocate memory for head
// insert Nodes with corresponding integer values one by one
