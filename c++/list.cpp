
#include <iostream>
using namespace std;

class PyList {
private:
    int* data;
    int currentSize;
    int currentCapacity;

    void resize() {
        currentCapacity *= 2;

        int* newData = new int[currentCapacity];

        for (int i = 0; i < currentSize; i++) {
            newData[i] = data[i];
        }

        delete[] data;
        data = newData;
    }

public:
    PyList() {
        currentSize = 0;
        currentCapacity = 2;
        data = new int[currentCapacity];
    }

    void append(int value) {
        if (currentSize == currentCapacity) {
            resize();
        }

        data[currentSize] = value;
        currentSize++;
    }

    int get(int index) {
        if (index < 0 || index >= currentSize) {
            throw out_of_range("Invalid index");
        }

        return data[index];
    }

    void set(int index, int value) {
        if (index < 0 || index >= currentSize) {
            throw out_of_range("Invalid index");
        }

        data[index] = value;
    }

    void pop() {
        if (currentSize > 0) {
            currentSize--;
        }
    }

    int size() {
        return currentSize;
    }

    int capacity() {
        return currentCapacity;
    }

    void display() {
        cout << "[";
        for (int i = 0; i < currentSize; i++) {
            cout << data[i];
            if (i < currentSize - 1) cout << ", ";
        }
        cout << "]\n";
    }

    ~PyList() {
        delete[] data;
    }
};

int main() {
    PyList nums;

    nums.append(10);
    nums.append(20);
    nums.append(30);

    nums.display();

    cout << "Size: " << nums.size() << endl;
    cout << "Capacity: " << nums.capacity() << endl;

    nums.set(0, 99);
    nums.display();

    nums.pop();
    nums.display();
}




#include <iostream>
using namespace std;

class PyList {
private:
    int* data;
    int current_size;
    int current_capacity;

public:
    PyList() {
        // TODO: Initialize an empty list
    }

    void append(int value) {
        // TODO: Check whether capacity is full
        // TODO: Increase capacity if needed
        // TODO: Insert the value
    }

    int get(int index) {
        // TODO: Return element at index
    }

    int size() {
        // TODO: Return current size
    }

    int capacity() {
        // TODO: Return current capacity
    }

    ~PyList() {
        // TODO: Free allocated memory
    }
};

int main() {
    PyList numbers;

    numbers.append(10);
    numbers.append(20);
    numbers.append(30);

    cout << numbers.get(0) << endl;
    cout << numbers.get(1) << endl;
    cout << numbers.get(2) << endl;

    cout << "Size: " << numbers.size() << endl;
    cout << "Capacity: " << numbers.capacity() << endl;

    return 0;
}
