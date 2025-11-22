#include <iostream>
using namespace std;

class Geometry{
    public:
    double areaRectangle(double a, double b){
        return a*b;
    };
    double peremiterRectangle(double a, double b){
        return 2*a+2*b;
    };
};

int main(){
    Geometry g1;
    double a1,b1;
    cout << "Enter the height of the rectangle : "; cin >> a1;
    cout << "Enter the length of the rectangle : "; cin >> b1;
    cout << "The area of the rectangle is : " << g1.areaRectangle(a1,b1) << endl;
    cout << "The peremiter of the rectangle is : " << g1.peremiterRectangle(a1,b1);
};