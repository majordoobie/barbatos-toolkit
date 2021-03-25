#include <stdio.h>
#include <stdlib.h>
#include "token.h"


struct Token
{
    tokenType_t type;
    void *token;
};

Token_t *make_token(tokenType_t type)
{

    Token_t *new_node = (Token_t*)calloc(1, sizeof(Token_t));

    if (type == Operator)
    {
       new_node->token = (void *) '+';
       new_node->type = type;
    }
    else
    {
        new_node->token = (void *) 10;
        new_node->type = type;
    }
    printf("Value is %d", (int *)new_node->token);

    return new_node;
}