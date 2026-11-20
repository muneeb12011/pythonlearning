#include <iostream> 
#include <list>
using namespace std;

int main() {
    list<int> my_list;
    my_list.push_back(1);
    my_list.push_back(2);
    my_list.push_back(3);

    for (const auto& element : my_list) {
        cout << element << " ";
    }
    cout << endl;

    return 0;
}
