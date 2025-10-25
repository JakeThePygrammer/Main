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
    int day, month, year;
    int currentday,currentmonth,currentyear;
    cout << "Enter day: ";
    cin >> day;
    cout << "Enter month: ";
    cin >> month;
    cout << "Enter year: ";
    cin >> year;
    cout << "Enter current day: ";
    cin >> currentday;
    cout << "Enter current month: ";    
    cin >> currentmonth;
    cout << "Enter current year: ";
    cin >> currentyear;

    int totaldays = 0;

    for(int i = year; i < currentyear; i++){
        for(int j = 1; j <= 12; j++){
            totaldays += monthyear(j, i);
        }
    }
    for(int j = 1; j < month; j++){
        totaldays -= monthyear(j, year);
    }
    for(int j = 1; j < currentmonth; j++){
        totaldays += monthyear(j, currentyear);
    }
    totaldays += (currentday - day);

    cout << "Total days between: " << totaldays << endl;
    return 0;
}
