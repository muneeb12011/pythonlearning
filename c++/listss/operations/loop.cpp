#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
 


int main() {
    vector<int> nums = {10, 20, 30};
    for (int x : nums) cout << x << " ";
    cout << endl;
    for (size_t i = 0; i < nums.size(); i++)
        cout << i << ": " << nums[i] << endl;
}