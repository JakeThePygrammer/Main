#include <iostream>
using namespace std;

void spacechecker(string text, char input) {
    int length = text.length();
    for (int i = 0; i < length; i++) {
        if (text[i] == input) {
            cout << i + 1 << endl;
        }
    }
}

int main() {
    string b;
    char a;
    cin >> b;
    cin >> a;
    spacechecker(b, a);
    return 0; 
}