#include <iostream>
#include <string>
using namespace std;

int main() {
    int arr[] = { 13,7,24,74,35,10,6,2,3,1 };
    int arrsize = 10;
    bool flag = true;
    while (flag) {
        flag = false;
        for (int i = 0; i < arrsize - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                int tempval = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tempval;
                flag = true;
            }
        }
    }
    for (int i = 0; i < arrsize; i++) cout << arr[i] << " ";
    cout << endl;
}
