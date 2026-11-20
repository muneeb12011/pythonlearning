#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    vector<int> nums = {10, 20, 30};
    nums[0] = 5;
    for (int n : nums) cout << n << " ";
    cout << endl;
}