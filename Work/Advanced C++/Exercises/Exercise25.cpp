#include <iostream>
#include <cmath>
using namespace std;

class Rectangularprism {
private:
    int x1, y1, z1, x2, y2, z2, l, w, h;

    void setlwh(int xx1, int yy1, int xx2, int yy2,int zz1,int zz2){
    l = abs(xx2 - xx1);
    w = abs(yy2 - yy1);
    h = abs(zz1-zz2);
    }
    

public:
    Rectangularprism(int xx1, int yy1, int xx2, int yy2, int zz1,int zz2){
        x1 = xx1;
        y1 = yy1;
        x2 = xx2;
        y2 = yy2;
        z1 = zz1;
        z2 = zz2;
    }
    float volume(){
        setlwh(x1, y1, x2, y2, z1, z2);
        return l * w * h;
        }
    float area(){
        setlwh(x1, y1, x2, y2, z1, z2);
        return 2*(l * w + w * h + h *l);
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
    int x,y,x1,y1,z1,z2;
    cout << "Enter the first x value : ";
    cin >> x;
    cout << "Enter the second x value : ";
    cin >> x1;
    cout << "Enter the first y value : ";
    cin >> y;
    cout << "Enter the second y value : ";
    cin >> y1;
    cout << "Enter the first z value : ";
    cin >> z1;
    cout << "Enter the second z value : ";
    cin >> z1;
    Rectangularprism rect(x, x1, y, y1, z1, z2);
    cout<<"Area: "<<rect.area()<<endl;
    cout<<"Volume: "<<rect.volume()<<endl;
    return 0;
}

