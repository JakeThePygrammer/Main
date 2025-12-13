#include <iostream>
using namespace std;

int NZD(int a, int b){
    int NZDvalue = 1;
    int smaller;
    if (a < b) smaller = a;
    else smaller = b;
    for (int i = smaller; i >= 1; i--) {
        if (a % i == 0 && b % i == 0) {
            NZDvalue = i;
            break;
        }
    }
    return NZDvalue;
}

int main(){
    int a, b;
    cout << "Enter number 1: ";
    cin >> a;
    cout << "Enter number 2: ";
    cin >> b;
    cout << "The largest common divisor of " << a << " and " << b << " is " << NZD(a,b) << endl;
    return 0;
}
