#include <stdio.h>

int main(){
    int c, a, b;
    
    scanf("%d", &c);

    for(int x = 0; x <c; x++){    
        scanf("%d%d", &a, &b);
        printf("%d\n", a + b);
    }

}