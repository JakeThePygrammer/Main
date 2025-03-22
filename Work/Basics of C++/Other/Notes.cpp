#include <iostream> //Preprocessor instructions
#include <cmath> // For squared
//Libraries are above this line
using namespace std;

int main(){
    string abc = "Input\nsome\ntext:"; //Initialize value
    /*Value types(defaut value if empty is 0)
    String - text(uses "", not '')
    Char - single character, uses ascii table for values,g + g = 206(we add the ascii values together),(uses '', not "")
    Int - number(using long long increases max size(max is 2^31-1 without long))
    Float/double - decimals(float - 32bit, double - 64bit)
    We must add a value type or it will not work
    */cout << abc << endl; //Output
    cin >> abc;  //Input
    cout << "\nYour\ntext\nis:\n" << "'" << abc << "'" << endl; //Combined output and /n for new line
    cout << "\nAscii\ntogether\nis:\n" << 'a' + 'a' << endl; //ascii values will be outputted
    /*Math operators(adding equal before to write to value)
    + - addition
    - - subtraction
    / - division
    * - multiplication
    % - remainder of division
    pow(number we want to square, number we square by) - squared (uses cmath library)
    */char n = 'A' + 3; // Char with integer
    cout << "\nInteger\nwith\nchar:\n" << n << endl; //Gives d because a-b-c-d(uses ascii values), if direct addition, will give direct ascii value.
    int a = 2;
    if (a == 1 || a == 2) cout << "\nA = 1 or 2." << endl;
    else cout << "\nA is not equal to 1 or 2." << endl;
    int finalnumber = 0;
    for(int currentnumber = 0; currentnumber < 1000; currentnumber++){ //For loops are useful, they can shorten code.
        if(currentnumber % 3 == 0 || currentnumber % 5 == 0) finalnumber += currentnumber; //If there is only 1 command, you can do it like this.
        /*If statement usable operators
        < - smaller than
        > - larger than
        == - equal to
        ++ - plus 1
        -- - minus 1
        =< - smaller than or equal to
        => - larger than or equal to
    */}
    cout << "\nThe\nfinal\nnumber\nis:\n" << finalnumber << endl;
}