#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    vector<int> nums = {10, 20, 30};
    reverse(nums.begin(), nums.end());
    for (int n : nums) cout << n << " ";
    cout << endl;
}