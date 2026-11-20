#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    vector<string> words = {"apple", "banana"};
    words.push_back("kiwi");
    string w = words[1];
    cout << w[0] << " " << w.back() << " " << w + "!" << endl;
    cout << words.size() << " words" << endl;
}