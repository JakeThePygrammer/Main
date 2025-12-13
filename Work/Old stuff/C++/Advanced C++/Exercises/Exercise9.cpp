#include <iostream>
using namespace std;

int main() {
    int matrix[3][2] = {
    {1,2},
    {2,3},
    {1,2}
    };
    int matrix1[3][2] = {
    {0,1},
    {2,-1},
    {-1,2}
    };
    cout << "Both matrixes subtracted : " << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 2; j++) {
            int razlika = matrix[i][j]-matrix1[i][j];
            cout << razlika << " ";
        }
        cout << endl;
    }

}
