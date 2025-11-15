#include <iostream>
using namespace std;

int getspecificdigit(int number, int position){
    int num = number / position;
    return num % 10;
}

int digitcollected(int number){
    int brojac = 0;
    int tally = 0;
    int position = 1;

    while (number / position > 0) {
        tally += getspecificdigit(number, position);
        position *= 10;
        brojac++;
    }

    return tally;
}

int main(){
    cout << digitcollected(1234) << endl; 
    return 0;
}
