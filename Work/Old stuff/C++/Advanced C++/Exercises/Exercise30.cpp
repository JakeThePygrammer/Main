#include <iostream>
using namespace std;

class Time{
    private:
        int hours;
        int minutes;
        int seconds;
    public:
        Time(int h, int m, int s){
            hours = h;
            minutes = m;
            seconds = s;
        };
        int secondscalc(){
            int secondscalcval = 0;
            secondscalcval += hours * 3600;
            secondscalcval += minutes * 60;
            secondscalcval += seconds;
            return secondscalcval;
        };
};

int main(){
    Time t1(5,15,30);
    cout << t1.secondscalc();
}