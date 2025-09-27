#include <iostream>

using namespace std;

int main()
{
    int A[10];

    for(int i=0;i<10;i++){
        cout<<"Enter list item "<< i+1 << " : ";cin>>A[i];
    }
    cout << "Only even numbers from list : ";
    for(int i=0;i<10;i++){
        if(A[i]% 2 == 0){
            cout <<A[i]<< " ";
        }

    }
    return 0;
}

