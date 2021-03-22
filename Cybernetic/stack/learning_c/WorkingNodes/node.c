#include <stdio.h>
#include "node.h"

node make_node(int value)
{
    node temp = {value};
    printf("%p\n", &temp);
    return temp;
}

node *make_node_prt(int value)
{
    node temp = {value};
    printf("%p\n", &temp);
    return &temp;
}