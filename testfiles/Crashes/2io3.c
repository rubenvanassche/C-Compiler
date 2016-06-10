#include <stdio.h>

int main()
{
    char s[10];
    int i = -1;
    printf("Type something: ");
    scanf("%s", s);
    printf("%10s %3d %3i %4c\n", s, i, i, s[0]);

    //return 0;
}
