#include <iostream>
using namespace std;

int main()
{
    int rows, columns, positive = 0, negative = 0, zeros = 0;
    cout << "Enter number of rows: ";
    cin >> rows;
    cout << "Enter number of columns: ";
    cin >> columns;
    int J[rows][columns];
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            cout << "Enter element [" << i << "][" << j << "]: ";
            cin >> J[i][j];
        }
    }
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            if(J[i][j] > 0){
                positive++;
            }
            else if(J[i][j] < 0){
                negative++;
            }
            else if(J[i][j] == 0){
                zeros++;
            }
        }
    }
    cout << "Number statistics in matrix:" << endl;
    cout << "Positive numbers: " << positive << endl;
    cout << "Negative numbers: " << negative << endl;
    cout << "Zeros: " << zeros << endl;
    
    return 0;
    }
