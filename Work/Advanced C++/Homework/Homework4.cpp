#include <iostream>
using namespace std;

int main()
{
int rows, columns;
cout << "Enter number of rows: ";
cin >> rows;
cout << "Enter number of columns: ";
cin >> columns;
int k=0;
int A[rows][columns];
int list[rows*columns];
for(int i=0;i<rows;i++){
    for(int j=0;j<columns;j++){
        cout<<"Enter element ("<<i<<","<<j<<"): ";
        cin>>A[i][j];
        list[k++]=A[i][j];
    }
}
    for (int i = 0; i < rows * columns - 1; i++) {
        for (int j = 0; j < rows * columns - i - 1; j++) {
            if (list[j] > list[j + 1]) {
                int tempval = list[j];
                list[j] = list[j + 1];
                list[j + 1] = tempval;
            }
        }
    }

int B[rows][columns];
int l=0;
for(int i=0;i<rows;i++){
    for(int j=0;j<columns;j++){
        B[i][j]=list[l++];
    }
}

cout<<"The sorted matrix is: "<<endl;
for(int i=0;i<rows;i++){
    for(int j=0;j<columns;j++){
        cout<<B[i][j]<<" ";
    }
    cout<<endl;
}
return 0;       
}