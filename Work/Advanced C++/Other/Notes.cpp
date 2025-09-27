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

//Symmetric matrixes

int A[3][3] = 
{
    {1,4,0},
    {4,-1,1},
    {0,1,0}
};

bool isSymmetric = true;
for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
        if(A[i][j]!=A[j][i]){
            isSymmetric = false;
            break;
        }
    }
}

//Multiplying matrixes(transpondent matrixes)

int main(){
    int rows1=2, columns1 = 3, rows2=3, columns2=2;
    int A[rows1][columns1] = {
        {1,2,3},
        {4,5,6}
    };
    int B[rows2][columns2] = {
        {7,8},
        {9,10},
        {11,12}
    };
    int C[2][2] = {
        {0,0},
        {0,0}
    };
    for(int i=0;i<rows1;i++){
        for(int j=0;j<columns2;j++){
            for(int k=0;k<columns1;k++){
                C[i][j] += A[i][k] * B[k][j];
                //cout << i << " - i " << j << " - j " << k << " - k " << endl;
                //Use to visualize the for cycles
            }
        }
    }
    for(int i=0;i<rows1;i++){
        for(int j=0;j<columns2;j++){
            cout<<C[i][j]<<" ";
        }
        cout<<endl;
    }
}

//Switching rows in a matrix

int A[3][3] = 
{
    {1,1,1},
    {2,2,2},
    {3,3,3}
};
for(int i=0;i<3;i++){
    int temp = A[0][i];
    A[0][i] = A[2][i];
    A[2][i] = temp;
}

//Switching columns in a matrix 
int A[3][3] = 
{
    {1,1,1},
    {2,2,2},
    {3,3,3}
};
for(int i=0;i<3;i++){
    int temp = A[i][0];
    A[i][0] = A[i][2];
    A[i][2] = temp;
}