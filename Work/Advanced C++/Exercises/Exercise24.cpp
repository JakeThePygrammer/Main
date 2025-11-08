#include <iostream>
#include <cmath>
using namespace std;

class Rectangle {
private:
    int x1, y1, x2, y2;
    

public:
    Rectangle(int xx1, int yy1, int xx2, int yy2){
        x1 = xx1;
        y1 = yy1;
        x2 = xx2;
        y2 = yy2;
    }
    int area(){
        return abs((x2 - x1) * (y2 - y1));
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
    Rectangle rect(1, 4, 4, 1);
    cout<<"Area: "<<rect.area()<<endl;
    return 0;
}

