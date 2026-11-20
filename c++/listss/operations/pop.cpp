#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


int main() {
    vector<int> nums = {10, 20, 30};
    int last = nums.back();
    nums.pop_back();
    cout << "removed " << last << ", size now " << nums.size() << endl;
}