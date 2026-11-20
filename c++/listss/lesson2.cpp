#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> fruits;

    fruits.push_back("apple");
    fruits.push_back("banana");
    fruits.push_back("mango");

    cout << "count: " << fruits.size() << endl;
    cout << "first: " << fruits[0] << endl;

    for (int i = 0; i < fruits.size(); i++) {
        cout << i << ": " << fruits[i] << endl;
    }
}