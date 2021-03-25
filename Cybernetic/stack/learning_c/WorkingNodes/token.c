#include <stdio.h>
#include <stdlib.h>
#include "token.h"


struct Token
{
    int value;
    enum tokenTypes type_type;
    void *token;
};

Token_t *make_token(tokenType_t type)
{

    Token_t *new_node = (Token_t*)calloc(1, sizeof(Token_t));

    if (type == Operator)
    {
       *(new_node->token) =  10
    }
    new_node->token = 10;
    return new_node;
}