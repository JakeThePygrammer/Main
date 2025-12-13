#include <iostream>
using namespace std;

int digitcounter(int number){
    int brojac = 0;

    while (number > 0) {
        number /= 10;
        brojac++;
    }

    return brojac;
}

int main(){
    int a;
    cout << "Enter a number : " ; cin >> a;
    cout << "The number of digits in your number is : " << digitcounter(a) << endl;
}