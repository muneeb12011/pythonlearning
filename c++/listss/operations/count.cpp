#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


int main() {
    vector<int> nums = {2, 5, 2, 7, 2};
    cout << count(nums.begin(), nums.end(), 2) << endl;
}