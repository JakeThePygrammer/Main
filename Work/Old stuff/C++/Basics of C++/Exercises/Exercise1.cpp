#include <iostream>
using namespace std;
int main()
{
    int a = 55;
    cout << "Kolku poeni imas : " , cin >> a;
    if(a > 60){
        cout << "Projde" << endl;
    }
    else{
        cout << "Padna" << endl;
    }
}