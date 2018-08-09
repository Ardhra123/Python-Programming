
#include <iostream>
using namespace std;
 
void printEvenNums(int n)
{
    int num = 1;
    int x = 2;
    while (even <= n) {
        cout << even << " ";
 
        
        even =even * x;
 
        x++;
    }
}
 

int main()
{
    int n = 100;
    printEvenNums(n);
    return 0;
}
