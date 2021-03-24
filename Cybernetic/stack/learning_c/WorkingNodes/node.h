typedef struct
{
    int value;
    struct Node_var *left;
    struct Node_var *right;

} Node;

Node *make_node(int value, Node *head_node);
void to_string(Node *node);
void iter_nodes(Node *head_node);
Node *get_last_node(Node *head_node);
void free_nodes(Node *head_node);