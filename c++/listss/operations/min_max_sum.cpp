#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    vector<int> nums = {10, 20, 30};
    cout << *min_element(nums.begin(), nums.end()) << endl;
    cout << *max_element(nums.begin(), nums.end()) << endl;
    int total = 0;
    for (int n : nums) total += n;
    cout << total << endl;
}