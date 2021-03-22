typedef struct Node
{
    int value;
    struct Node *left;
    struct Node *right;

} Node;

struct Node *make_node(int value, Node *right_node);
void to_string(Node *node);