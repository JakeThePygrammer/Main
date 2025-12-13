#include <iostream>
#include <fstream>
using namespace std;
int main() {
    string text = "abc";
    while(text != "END"){
        cout << "Enter file name (or END to stop): ";
        cin >> text;
        ofstream file(text + ".txt");
        file.close();
    }
    return 0;
}