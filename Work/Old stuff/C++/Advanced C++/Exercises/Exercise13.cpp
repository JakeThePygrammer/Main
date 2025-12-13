#include <iostream>
 
using namespace std;
 
int main()
{
    int gradovi[7][7] ={
        {0,1,0,0,0,0},
        {1,0,1,0,0,0},
        {0,1,0,0,1,1},
        {0,0,0,0,0,0},
        {0,1,0,0,0,0},
        {0,0,1,0,0,0},
        {0,0,1,0,0,0},
    };
 
    int grad1=0;
    int grad2=0;
    cout<<"Vnesi grad!"<<endl;
    cin>>grad1;
    cout<<"Vnesi grad!"<<endl;
    cin>>grad2;
 
    bool flag = true;
 
 
    for(int i=0; i<7; i++){
        for(int j=0; j<7; j++){
            if(i==grad1 && j==grad2){
                if(gradovi[i][j] != 1){
                    flag=false;
                    break;
                }
            }
            if(i==grad2 && j==grad1){
                if(gradovi[i][j] != 1){
                    flag=false;
                    break;
                }
            }
        }
    }
 
    if(flag==true){
        cout<<"Postoi vrska!"<<endl;
    }else{
        cout<<"Nepostoi vrska!"<<endl;
    }
 
    return 0;
}