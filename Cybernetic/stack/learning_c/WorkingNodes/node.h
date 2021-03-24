typedef struct
{
    int value;
    struct Node_var *left;
    struct Node_var *right;

} Node;

struct Nod2
{
    int value;
    struct Node_var *left;
    struct Node_var *right;

};

typedef Nod2 Nodet;

Node *make_node(int value, Node *head_node);
void to_string(Node *node);
void iter_nodes(Node *head_node);
Node *get_last_node(Node *head_node);
void free_nodes(Node *head_node);