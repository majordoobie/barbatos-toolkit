#include <stdio.h>

#define FOO 4
#define str(s) #s
#define stringify(s) str(s)

int main(void)
{
  
  printf("%d\n", FOO);
  printf("%s\n", str(FOO));
  printf("%s\n", stringify(FOO));
}
