#include <stdio.h>

int main() {
    int i = 56;
    int j = 138;
    printf(" value of i=%d j=%d before swapping", i, j);

    i = i ^ j;
    j = i ^ j;
    i = i ^ j;
    printf("value of i=%d j=%d after swapping", i, j);

    return 0;
}
