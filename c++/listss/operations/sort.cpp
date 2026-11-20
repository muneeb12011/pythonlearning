#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
  



int main() {
    vector<int> nums = {30, 10, 20};
    sort(nums.begin(), nums.end());
    for (int n : nums) cout << n << " ";
    cout << endl;
    sort(nums.rbegin(), nums.rend());
    for (int n : nums) cout << n << " ";
    cout << endl;
}