#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    vector<int> a = {1, 2, 3};
    vector<int> b = a;          // in c++ this is a reall copy
    b.push_back(4);
    cout << "a size " << a.size() << ", b size " << b.size() << endl;
}