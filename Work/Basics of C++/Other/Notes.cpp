#include <iostream> //Preprocessor instructions
#include <cmath> // For squared
//Libraries are above this line
using namespace std;

double proba(int stolche = 1, float stolche2 = 1.1, string ime = "abc"){
    cout << "|";
    for(int i = 0; i < ime.length(); i++){
        cout << ime[i] << "|";
    } cout <<endl;
    return (double) stolche * stolche2;
}
    //Function creation(the start of the function determies the end value type)
int main(){
    cout << proba(5, 3.5, "abcdefgh") <<endl;
    //Calling self-made function
    string abc = "Input\nsome\ntext:"; //Initialize value
    /*Value types(defaut value if empty is 0)
    String - text(uses "", not '')
    Char - single character, uses ascii table for values,g + g = 206(we add the ascii values together),(uses '', not "")
    Int - number(using long long increases max size(max is 2^31-1 without long))
    Float/double - decimals(float - 32bit, double - 64bit)
    Bool - true/false
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
    const int numberconst = 0
    //Using const is useful when you don't want to change a variable after creation.
    int list1[10] = {10,20,30,40,50};
    list1[5] = 60;
    list1[6] = 70;
    list1[7] = 80;
    list1[8] = 90;
    list1[9] = 100;
    //Lists can only have 1 value type, and their values can be declared in 2 ways.
    string t2 = "hello";
    cout << t2.length() << endl;
    //This gives us the length of the string.
    getline(cin, t2);
    //This stops the inout on a new line, not on a space.
    for (int i = 0; i < 10:i++);
    /*For cycles work like this:
    The first space is used for something that is only done at the start of the for(usually to initialize the variable)
    The second space is used for the condition(like in while or if)
    The third space is something that runs at the end of every cycle(usually used to add to the variable)
    Tip : you can use stuff other than ++, such as
    -- to go down by one
    _= so that you can do the operation by using a specific number
    There are other options such as multiplication and division
    */
   }

