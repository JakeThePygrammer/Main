#include <iostream>
#include <fstream>
using namespace std;
float Calc(float broj1, float broj2,string calcval){
    if(calcval == "*")
        return broj1*broj2;
    else if(calcval == "/")
        return broj1/broj2;
    else if(calcval == "+")
        return broj1+broj2;
    else if(calcval == "-")
        return broj1-broj2;
}
int main(){
    float a,b;
    string c;
    cout<<"Enter first number: ";
    cin>>a;
    cout<<"Enter second number: ";
    cin>>b;
    cout<<"Enter action(+,-,*,/): ";
    cin>>c;
    cout<<a<<c<<b<<"="<<Calc(a,b,c)<<endl;
}
