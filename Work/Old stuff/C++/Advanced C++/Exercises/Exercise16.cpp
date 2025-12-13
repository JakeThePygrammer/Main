#include <iostream>
#include <fstream>
using namespace std;
int Pogolem(int broj1, int broj2){
    if(broj1 > broj2)return broj1;
    else return broj2;
}
int main(){
    int a=4,b=5,c=2;
    int m1=Pogolem(a,b);
    int m2=Pogolem(m1,c);
    cout<<m2<<endl;
    return 0;
}
