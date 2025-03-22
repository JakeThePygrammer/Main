#include <iostream>
using namespace std;
int main(){
    int a = 2;
    if (a == 1 || a == 2) cout << "\nA = 1 or 2." << endl;
    else cout << "\nA is not equal to 1 or 2." << endl;
    int finalnumber = 0;
    for(int currentnumber = 0; currentnumber < 1000; currentnumber++){ 
        if(currentnumber % 3 == 0 || currentnumber % 5 == 0) finalnumber += currentnumber; 
    }
    cout << "\nThe\nfinal\nnumber\nis:\n" << finalnumber << endl;
}