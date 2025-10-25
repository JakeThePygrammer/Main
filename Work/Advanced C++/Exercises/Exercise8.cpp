#include <iostream>
using namespace std;

int main() {
    int red, kol, total;
    cout << "Enter the amount of rows in the matrix: ";
    cin >> red;
    cout << "Enter the amount of columns in the matrix: ";
    cin >> kol;
    int matrix[red][kol];
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << "Enter value [" << i << "][" << j << "]: ";
            cin >> matrix[i][j];
        }
    }
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {

                if(i==j)total += matrix[i][j];
        }
    }
    cout<<"Sum of all values in the diagonal is : "<<total<<endl;
}
