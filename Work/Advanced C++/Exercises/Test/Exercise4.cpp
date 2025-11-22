#include <iostream>
using namespace std;

void pozdrav(string ime){
    cout << "Zdravo " << ime << "!" << endl;
}

int main(){
    string ime1;
    cout << "Vnesi ime : "; cin >> ime1;
    pozdrav(ime1);
}