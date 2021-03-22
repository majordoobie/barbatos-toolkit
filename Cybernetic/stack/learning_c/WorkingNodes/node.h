typedef struct Node
{
    int value;
    struct Node *left;
    struct Node *right;

} Node;

struct Node make_node(int value);
struct Node *make_node_ptr(int value, Node *right_node);