#include <iostream>
#include <cmath>
using namespace std;

class Rectangle {
private:
    int x1, y1, x2, y2, a, b;
    

public:
    Rectangle(int xx1, int yy1, int xx2, int yy2){
        x1 = xx1;
        y1 = yy1;
        x2 = xx2;
        y2 = yy2;
    }
    void setAB(int xx1, int yy1, int xx2, int yy2){
        a = abs(xx2 - xx1);
        b = abs(yy2 - yy1);
    }
    float area(){
        setAB(x1, y1, x2, y2);
        return a * b;
    }
    int TopCornerX(){
        return x1;
    }
    int TopCornerY(){
        return y1;
    }
    int BottomCornerX(){
        return x2;
    }
    int BottomCornerY(){
        return y2;
    }
    void topcornerchange(int newx1, int newy1){
        x1 = newx1;
        y1 = newy1;
    }
    void bottomcornerchange(int newx2, int newy2){
        x2 = newx2;
        y2 = newy2;
    }
};

int main() {
    int x,y,x1,y1;
    cout << "Enter the top corner x value : ";
    cin >> x;
    cout << "Enter the top corner y value : ";
    cin >> y;
    cout << "Enter the bottom corner x value : ";
    cin >> x1;
    cout << "Enter the bottom corner y value : ";
    cin >> y1;
    Rectangle rect(x, y, x1, y1);
    cout<<"Area: "<<rect.area()<<endl;
    return 0;
}

