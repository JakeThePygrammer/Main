#include <iostream>
using namespace std;
int main()
{
    int sumof3and5 = 0;
    int currentnumber = 1;
    while (currentnumber < 1000){
        if(currentnumber % 5 == 0){
            sumof3and5 += currentnumber;
            currentnumber += 1;
        }
        else{
            if(currentnumber % 3 == 0){
                sumof3and5 += currentnumber;
                currentnumber += 1;
            }
            else{
                currentnumber += 1;
            }
        }
    }
cout << sumof3and5 << endl;
}