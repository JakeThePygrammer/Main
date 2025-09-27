#include <iostream>
using namespace std;

int main() {
    int rows, columns;
    cout << "Enter the amount of rows in the matrix: ";
    cin >> rows;
    cout << "Enter the amount of columns in the matrix: ";
    cin >> columns;
    cout << "Enter the number to multiply the matrix by: ";
    int number;
    cin >> number;
    int matrix[rows][columns];

    int matrixcol[rows][columns];
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            cout << "Enter value [" << i << "][" << j << "] for the matrix: ";
            cin >> matrix[i][j];
            matrixcol[i][j] = matrix[i][j] * number;
        }
    }
    cout << "The resulting matrix is: " << endl;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            cout << matrixcol[i][j] << " ";
        }
        cout<<endl;
    }
}