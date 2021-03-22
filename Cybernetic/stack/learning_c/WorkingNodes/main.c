#include <stdio.h>
#include "Node.h"


int main(int argc, char **argv)
{

    Node one = make_Node(10);
    printf("%p\n", &one);

    return 0;
}







// allocate memory for head
// insert Nodes with corresponding integer values one by one
