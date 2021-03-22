#include <stdio.h>
#include "node.h"

int main(int argc, char **argv)
{
    // allocate memory for head
    // insert nodes with corresponding integer values one by one

    node one = make_node(10);
    printf("%p\n", &one);

    return 0;
}
