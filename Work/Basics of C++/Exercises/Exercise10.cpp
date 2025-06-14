#include <iostream>
#include <string>
using namespace std;

int main() {
    int list[] = { 13,7,24,74,35,10,6,2,3,1 };
    int listsize = 10;
    bool flag = true;
    while (flag) {
        flag = false;
        for (int i = 0; i < listsize - 1; i++) {
            if (list[i] > list[i + 1]) {
                int tempval = list[i];
                list[i] = list[i + 1];
                list[i + 1] = tempval;
                flag = true;
            }
        }
    }
    for (int i = 0; i < listsize; i++) cout << list[i] << " ";
}
