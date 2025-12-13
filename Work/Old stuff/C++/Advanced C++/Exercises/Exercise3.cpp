#include <iostream>

using namespace std;

int main()
{
    int fibbonaci[10];

    for(int i=0;i<10;i++){
        if(i < 2)fibbonaci[i] = 1;
        else fibbonaci[i] = fibbonaci[i-1] + fibbonaci[i-2];
    }
    cout << "First 10 elements of the fibbonaci sequence : ";
    for(int i=0;i<10;i++)cout <<fibbonaci[i]<< " ";

}

