#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int a;
    cout << "Enter the size of the board: ";
    cin >> a;
    ofstream matrixs("matrix.txt");
    for (int i = 0; i < a; i++) {
        for (int j = 0; j < a; j++) {
            int var = i+j;
            if(var%2==0)matrixs << "#";
            else matrixs << "-";
    }
    matrixs << endl;
}
matrixs.close();
}