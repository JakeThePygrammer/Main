#include <iostream>
using namespace std;
int main() {
    int red, kol;
    cout << "Enter the amount of rows in the matrixes: ";
    cin >> red;
    cout << "Enter the amount of columns in the matrixes: ";
    cin >> kol;
    int matrix[red][kol];
    int matrix1[red][kol];
    int matrixcol[red][kol];
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << "Enter value [" << i << "][" << j << "] for matrix 1: ";
            cin >> matrix[i][j];
            cout << "Enter value [" << i << "][" << j << "] for matrix 2: ";
            cin >> matrix1[i][j];
            matrixcol[i][j] = matrix[i][j]+matrix1[i][j];
        }
    }
    cout << "Both matrixes combined : " << endl;
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << matrixcol[i][j] << " ";
        }
        cout<<endl;
    }
}
