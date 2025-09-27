#include <iostream>
using namespace std;

//This is the way that matrixes(2D lists) are created

int main() {
    int red, kol;
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
            cout << matrix[i][j] << " ";
        }
        cout<<endl;
    }
}

//This is how to only have diagonal values entered

int main() {
    int red, kol;
    cout << "Enter the amount of rows in the matrix: ";
    cin >> red;
    cout << "Enter the amount of columns in the matrix: ";
    cin >> kol;
    int matrix[red][kol];
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
        if(i==j){
            cout << "Enter value [" << i << "][" << j << "]: ";
            cin >> matrix[i][j];
        }
        else{
            matrix[i][j]=0;
        }
        }
    }
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << matrix[i][j] << " ";
        }
        cout<<endl;
    }
}

//For upper and lower triangle

//Upper triangle

for(int i=0: i < red;i++){
    for(int j=i;j<kol;j++){
        Q[i],[j]
        }
}

//Lower triangle

for(int i=0;i<red;i++){
    for(int j=0; j<=i;j++){
        Q[i][j]
    }
}

//Combining 2 matrixes

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
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << matrixcol[i][j] << " ";
        }
        cout<<endl;
    }
}
