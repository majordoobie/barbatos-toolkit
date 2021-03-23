typedef struct
{
    int value;
    struct Node_var *left;
    struct Node_var *right;

} Node_var;

Node_var *make_node(int value, Node_var *head_node);
void to_string(Node_var *node);
void iter_nodes(Node_var *head_node);
Node_var *get_last_node(Node_var *head_node);
void free_nodes(Node_var *head_node);