#include <iostream>
using namespace std;

int main() {
    int red, kol;
    cout << "Enter the amount of rows in the matrix: ";
    cin >> red;
    cout << "Enter the amount of columns in the matrix: ";
    cin >> kol;

    char Q[red][kol];

    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol - i; j++) {
            Q[i][j] = '*';
        }
        for (int j = kol - i; j < kol; j++) {
            Q[i][j] = ' ';
        }
    }

    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << Q[i][j];
        }
        cout << endl;
    }

    return 0;
}
