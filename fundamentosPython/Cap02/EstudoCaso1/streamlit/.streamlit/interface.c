#include <stdio.h>
#include "interface.h"

void menu(){
    printf("\n\t\t MENU\t\n\n");
    printf("Please enter a input: ");
    printf("\n\n[1]: OP 1");
    printf("\n[2]: OP 2");
    printf("\n[3]: OP 3");
    printf("\n[4]: OP 4");
    printf("\n[0]: Exit \n\n");
    

}

void looping(int b){
    while (b!= 0 ){
        menu();
        scanf("%d",&b);
    }
    

}