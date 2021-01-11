#include <stdio.h>

int main(){
    int a;

    scanf("%d", &a);

    for(int x = 1; x <10; x++){
        printf("%d * %d = %d\n", a, x, a*x);
    }
}