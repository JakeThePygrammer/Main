#include <iostream>
#include <string>
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

string shorteningfraction(int a, int b){   
    int nzd = NZD(a, b);
    a = a / nzd;
    b = b / nzd;
    string abc = to_string(a) + "/" + to_string(b);  
    return abc;
}

int main(){
    int numerator, denominator;
    cout << "Enter numerator (top): ";
    cin >> numerator;
    cout << "Enter denominator (bottom): ";
    cin >> denominator;

    string shortened = shorteningfraction(numerator, denominator);
    cout << "The shortened fraction is " << shortened << endl;
    return 0;
}
