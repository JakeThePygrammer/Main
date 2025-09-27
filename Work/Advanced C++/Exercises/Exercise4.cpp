#include <iostream>

using namespace std;

int main()
{
    int listlen1 = 0, listlen2 = 0, tally1 = 0, tally2 = 0;
    cout << "Enter first list length : ";cin >> listlen1;
    cout << "Enter second list length : ";cin >> listlen2;
    int A[listlen1], B[listlen2];
    for(int i=0;i<listlen1;i++){
        cout<<"Enter list item for list 1 item "<< i+1 << " : ";cin>>A[i];
        tally1 += A[i];
    }
    for(int i=0;i<listlen1;i++){
        cout<<"Enter list item for list 2 item "<< i+1 << " : ";cin>>B[i];
        tally2 += B[i];
    }
    cout<<"The 2 lists totals subtracted is equal to: ";
    if(tally1-tally2 < 0) cout<<tally2-tally1;
    else cout<<tally1-tally2;
    return 0;
}

