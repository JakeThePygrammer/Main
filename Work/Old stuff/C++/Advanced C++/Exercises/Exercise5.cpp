#include <iostream>
using namespace std;

int main() {
    string a;
    cout << "Enter your text: ";cin >> a;
    int stringlength = a.length();
    for (int i = 0; i < stringlength / 2; i++) {
        if (a[i] != a[stringlength - i - 1]) {
            cout << "Your text is not a palindrome";
            return 0;
        }
    }
    cout << "Your text is a palindrome";
}
