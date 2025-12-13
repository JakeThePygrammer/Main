#include <iostream>
using namespace std;
int monthyear(int month, int year){
    if(month == 4 || month == 6 || month == 9 || month == 11){
        return 30;
    }
    else if(month == 2){
        if((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)){
            return 29;
        }
        else{
            return 28;
        }
    }
    else{
        return 31;
    }
}
int main() {
    int month, year;
    cout << "Enter month: ";
    cin >> month;
    cout << "Enter year: ";
    cin >> year;
    int days = monthyear(month, year);
    cout << "Number of days in the month: " << days << endl;
    return 0;
}