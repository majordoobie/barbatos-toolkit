typedef struct Token Token_t;

typedef enum {Operator, Operand} tokenType_t;

Token_t *make_token(tokenType_t type);