#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int* p = new int(5);
    cout << "stack addr: " << &a << "\n";
    cout << "heap  addr: " << p << "\n";
    delete p;
}
