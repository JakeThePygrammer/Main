#include <iostream>
using namespace std;

int main() {
    string test1 = "Hello world! My name is CLW93.";
    int length = test1.length();
    for (int i = length - 1; i >= 0; i--) {
        cout << test1[i] << endl;
    }
    return 0;
}
