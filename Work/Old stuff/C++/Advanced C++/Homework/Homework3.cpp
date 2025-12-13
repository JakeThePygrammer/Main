#include <iostream>
using namespace std;

int main()
{
    int rows, columns;
    cout << "Enter number of rows: ";
    cin >> rows;
    cout << "Enter number of columns: ";
    cin >> columns;
    char J[rows][columns];
    char K[columns][rows]; 
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            cout << "Enter element [" << i << "][" << j << "]: ";
            cin >> J[i][j];
        }
    }
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            K[j][i] = J[i][j];
        }
    }
    cout << "Transponded matrix:" << endl;
    for(int i = 0; i < columns; i++){
        for(int j = 0; j < rows; j++){
            cout << K[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
