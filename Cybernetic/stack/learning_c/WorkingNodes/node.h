typedef struct
{
    int value;
    struct Node_var *left;
    struct Node_var *right;

} Node_t;

Node_t *make_node(int value, Node_t *head_node);
void to_string(Node_t *node);
void iter_nodes(Node_t *head_node);
Node_t *get_last_node(Node_t *head_node);
void free_nodes(Node_t *head_node);