#include <stdio.h>
#include <stdlib.h>

int main() {
    int vetor[100] = {[0]= 10,[49]=100};
    for(int i = 0; i < 100; i++) {
        printf("vetor[%d] = %d\n", i, vetor[i]);
    }       
}


