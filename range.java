#include <iostream>
using namespace std;
bool inRange(unsigned low, unsigned high, unsigned x)
{
return (low <= x && x <= high);
}

int main()
{
inRange(10, 100,40)? cout << "Yes\n": cout <<"No\n";
inRange(10, 100,15)? cout << "Yes\n": cout <<"No\n";
}

