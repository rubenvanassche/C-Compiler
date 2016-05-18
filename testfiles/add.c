#include <main.c>

int printf(char* x, int);

int main(){
    int i = 0;
    int sum = 0;

    for ( i = 1; i <= LAST; i++ ) {
      sum =  sum +i;
    } /*-for-*/
    printf("sum = %d\n", sum);

    return 0;
}
