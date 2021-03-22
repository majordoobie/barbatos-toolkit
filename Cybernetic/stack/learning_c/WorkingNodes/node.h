typedef struct node
{
    int value;
    struct node *left;
    struct node *right;

} node;

struct node make_node(int value);
struct node *make_node_ptr(int value);