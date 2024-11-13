// main.c
#include <stdio.h>
#include "add.h"

int main() {
    int a = 5;
    int b = 3;
    int result = add(a, b);
    printf("The result of %d + %d is %d\n", a, b, result);
    return 0;
}
