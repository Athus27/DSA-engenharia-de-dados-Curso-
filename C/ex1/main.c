// Iniciar um vetor de inteiros com 100 posições, onde a primeira posição
// (índice 0) é inicializada com o valor 10 e a posição de índice 49 é
// inicializada com o valor 100. As demais posições devem ser inicializadas com 0. Utilize
// a sintaxe de inicialização designada do C, resolver em apenas uma linha.




#include <stdio.h>
#include <stdlib.h>

int main() {
    int vetor[100] = {[0]= 10,[49]=100};
    for(int i = 0; i < 100; i++) {
        printf("vetor[%d] = %d\n", i, vetor[i]);
    }       
}




