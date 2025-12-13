#include <iostream>

using namespace std;

int main()
{
    int A[10];
    int tally = 0;

    for(int i=0;i<10;i++){
        cout<<"Enter list item "<< i+1 <<" (index "<<i<<")"<< " : ";cin>>A[i];
    }
    cout << "Only odd indexed numbers from list combined: ";
    for(int i=1;i<10;i+=2){
        tally += A[i];
    }
    cout << tally;
    return 0;
}

