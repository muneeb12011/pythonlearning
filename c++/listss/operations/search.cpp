#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
 


int main() {
    vector<int> nums = {10, 20, 30};
    auto it = find(nums.begin(), nums.end(), 20);
    if (it != nums.end())
        cout << "found at index " << (it - nums.begin()) << endl;
    else
        cout << "not found" << endl;
}