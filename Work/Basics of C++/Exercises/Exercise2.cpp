#include <iostream>
using namespace std;

int main(){
    int a,b,c;
    cout << "A: "; cin >> a;
    cout << "B: "; cin >> b;
    cout << "C: "; cin >> c;
    if(a == b && b == c){
        cout << "Aktiviran e IF" << endl;
    }
    else{
        cout << "Aktiviran e ELSE" << endl;
    }
}