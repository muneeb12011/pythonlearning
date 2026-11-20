#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;



int main() {
    vector<int> a = {1, 2};
    vector<int> b = {3, 4};
    a.insert(a.end(), b.begin(), b.end());
    for (int n : a) cout << n << " ";
    cout << endl;
}