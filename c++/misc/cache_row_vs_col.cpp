#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using Clock = chrono::steady_clock;

int main() {
    const int N = 4000;
    vector<int> m(N * N, 1);
    long long sum = 0;

    auto t0 = Clock::now();
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++) sum += m[r * N + c];
    auto t1 = Clock::now();
    for (int c = 0; c < N; c++)
        for (int r = 0; r < N; r++) sum += m[r * N + c];
    auto t2 = Clock::now();

    cout << "row by row: " << chrono::duration<double, milli>(t1 - t0).count() << " ms\n";
    cout << "col by col: " << chrono::duration<double, milli>(t2 - t1).count() << " ms\n";
    cout << sum << "\n";
}
