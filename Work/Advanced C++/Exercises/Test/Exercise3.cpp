#include <iostream>
using namespace std;
class Matematika{
    public:
    int faktoriel(int n){
        int tally = 1;
        for(int i = 1; i <= n; i++){
            tally *= i;
        }
        return tally;
    };
};

int main(){
    Matematika m1;
    int broj;
    cout << "Vnesi broj : "; cin >> broj;
    cout << "Faktoriel na vasiot broj e : " << m1.faktoriel(broj) << endl; 
}