#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int getspecificdigit(int number, int position){
    return (number / position) % 10;
}

int largestnumberpossiblewithdigits(int number){
    string numStr = to_string(number);
    int length = numStr.length();
    int digits[length];
    int largestNumber = 0;

    for(int i = 0; i < length; i++){
        digits[i] = getspecificdigit(number, pow(10, length - i - 1));
    }

    for(int i = 0; i < length - 1; i++){
        for(int j = 0; j < length - i - 1; j++){
            if(digits[j] < digits[j + 1]){
                int temp = digits[j];
                digits[j] = digits[j + 1];
                digits[j + 1] = temp;
            }
        }
    }

    for(int i = 0; i < length; i++){
        largestNumber = largestNumber * 10 + digits[i];
    }

    return largestNumber;
}

int main(){
    int number;
    cout << "Enter a number: ";
    cin >> number;
    cout << "Largest possible number: " << largestnumberpossiblewithdigits(number) << endl;
    return 0;
}
