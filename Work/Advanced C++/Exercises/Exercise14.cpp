#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream dava("izlez.txt");
    ifstream zima("vlez.txt");
    string tempval;
    while (!zima.eof()) {
        getline(zima, tempval);
        dava << tempval << endl;
    }
    dava.close();
    zima.close();
    ifstream readtext("izlez.txt");
    string lines;
    while (!readtext.eof()) {
        getline(readtext, lines);
        cout << lines << endl;
    }
    readtext.close();
    return 0;
}

