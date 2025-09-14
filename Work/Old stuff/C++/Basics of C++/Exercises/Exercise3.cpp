#include <iostream>

using namespace std;

int main(){
    int listing[10] = {10,20,30,40,50};
    listing[5] = 60;
    listing[6] = 70;
    listing[7] = 80;
    listing[8] = 90;
    listing[9] = 100;
    int a;
    cout << "Enter a list index from 1-10:";
    cin >> a;
    a -= 1;
    if (a >= 0 && a < 10){
        cout << "\nIn the list, the value connected to the index is:\n" << listing[a] << endl;
    }
    else{
        cout << "\nIndex out of range or not valid!\nInput value must be between 1-10 and without other characters!" << endl;
    }
}

