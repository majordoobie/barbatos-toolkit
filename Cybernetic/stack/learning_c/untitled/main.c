#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main() {
    char hostname[255];
    memset(hostname, 0, sizeof(hostname));
    gethostname(hostname, sizeof(hostname));
    printf("%s", hostname);
    printf("Hello, World!\n%s", hostname);
    return 0;
}
