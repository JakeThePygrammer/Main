#include <iostream>
using namespace std;
float prosekTri(float a, float b, float c){
    float prosek = a+b+c;
    return prosek/3;
}
int main(){
    float a,b,c;
    cin >> a >> b >> c;
    cout << prosekTri(a,b,c);
}
