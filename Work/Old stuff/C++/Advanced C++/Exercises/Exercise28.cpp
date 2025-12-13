#include <iostream>
using namespace std;

class Math {
    public:
    int squared(int n){
        return n*n;
    };
    int cubed(int n){
        return n*n*n;
    };

};

int main(){
    int a;
    cout << "Enter a number : ";cin >> a;
    Math abc;
    cout << "Number squared : " << abc.squared(a) << endl;
    cout << "Number cubed : " << abc.cubed(a) << endl;

}