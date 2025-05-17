#include <iostream>
using namespace std;

int pozchecker(int number,int poz){
    poz = (poz+1) * 10;
    number /= poz;
    return number % 10;
    }
int main(){
    cout << pozchecker(12232415,5) << endl;
}