#include <iostream>
using namespace std;

int zbir(int n){
int var = 0;
for(int i=1;i<=n;i++)var+=i;
return var;
}

int main(){
int val1;
cout<<"To how much do you want to add: ";cin>>val1;
cout<<"Result: "<<zbir(val1)<<endl;
}
