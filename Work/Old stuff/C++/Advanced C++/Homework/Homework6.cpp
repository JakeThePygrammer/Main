#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream dava("izlez.txt");
    string tempval;
    int amountoflines;
    cout<<"Enter the amount of lines you want to write to the file: ";
    cin>>amountoflines;
    for(int i=0;i<amountoflines;i++){
        cout<<"Enter name, surname and phone number for line "<<i+1<<": ";
        getline(cin, tempval);
        dava<<tempval<<endl;
    }
    dava.close();
    return 0;
}
