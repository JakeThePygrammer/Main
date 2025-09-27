#include <iostream>
using namespace std;
int main()
{
int rows, columns;
cout << "Enter number of rows: ";
cin >> rows;
cout << "Enter number of columns: ";
cin >> columns;

int A[rows][columns];

bool isSymmetric = true;
for(int i=0;i<rows;i++){
    for(int j=0;j<columns;j++){
        if(A[i][j]!=A[j][i]){
            isSymmetric = false;
            break;
        }
    }
}
if(isSymmetric)cout<<"The matrix is symmetric.";

else cout<<"The matrix is not symmetric.";
return 0;
}
