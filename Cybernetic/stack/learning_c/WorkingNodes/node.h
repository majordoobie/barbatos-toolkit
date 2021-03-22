typedef struct Node
{
    int value;
    struct Node *left;
    struct Node *right;

} Node;

struct Node make_Node(int value);
struct Node *make_Node_ptr(int value);