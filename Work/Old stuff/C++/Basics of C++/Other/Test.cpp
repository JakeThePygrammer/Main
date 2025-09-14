#include <iostream>
#include <string>
using namespace std;

string user[] = {"Administrator", "Marko", "testuser", "sqlsrv", "nikola"}; 
string pass[] = {"S%8k6p7-z0/F?rW7", "Password123", "test123", "zNB?Vm/AEL$nPi!&)?T0", "#pr0p4$$w0rd505"};

bool auth(string username, string password){
    for(int i = 0; i < 5; i++){
        if(username == user[i] && password == pass[i]) return true;
    }
    return false;
}

int user_id(string username){
    for(int i = 0; i < 5; i++){
        if(username == user[i]) return i;
    }
    return -1;
}




int main(){
    while(true){
        cout << "[=====(LOGIN)=====]" <<endl;
        string in_user, in_pass;
        int opt = 0;
        cout << "username: "; cin >> in_user;
        cout << "password: "; cin >> in_pass;
        int userides = user_id(in_user);
        if(!auth(in_user, in_pass)) cout << "ACCESS DENIED: bad username or password" <<endl;
        else if(userides == 0 && auth(in_user, in_pass)){ 
            while(true){
                cout << "[==============================================================]" <<endl;
                cout << "SYSTEM_MESSAGE: Succesfully logged in as Administrator" <<endl;
                cout << "1. Log Out" <<endl;
                cout << "2. List all users" <<endl;
                cout << "3. Change users password" <<endl;
                cout << "4. Change your username" <<endl;
                cout << "5. Change your password" <<endl;
                cout << "6. Sort Array" <<endl;
                cout << "7. Palindrome Test (int, string)" <<endl;
                cout << "8. Text Statistics" <<endl;
                cout << "0. Exit" <<endl;
                cout << "Select option: "; cin >> opt;
                if(opt == 1) {break;}
                else if(opt == 2) {for(int i = 0; i < 5;i++) cout << "Username " << user[i] << "Password " << pass[i] << endl;}
                else if(opt == 3) {
                    string selectuser = "";
                    int selectuserid = 6;
                    string selectpass = "";
                    cout << "Select a user:"; cin >> selectuser;
                    for(int i = 0; i < 5; i++){
                        if(selectuser == user[i]){
                            selectuserid = i;
                        }
                        }
                    if(selectuserid = 6)cout << "Incorrect username!";
                    else{
                        cout << "Input password:"; cin >> selectpass;
                            pass[selectuserid] = selectpass;
                    }
                    }
                else if(opt == 4) {
                    string newadminuser = "";
                    cout << "New username "; cin >> newadminuser;
                    user[0] = newadminuser;
                }
                else if(opt == 5) {
                    string newadminpass = "";
                    cout << "New password "; cin >> newadminpass;
                    pass[0] = newadminpass;
                }
                else if(opt == 6) {
                    int listsize = 0;
                    cout << "Enter your list length "; cin >> listsize;
                    int sortlist[listsize] = {};
                    for(int i = 0;i < listsize;i++){
                        int tempval = 0;
                        cout << "Enter value "; cin >> tempval;
                        sortlist[i] = tempval;
                    }
                    bool flag = true;
                    while(flag){
                        flag = false;
                        for(int i = 0;i < listsize - 1; i++){
                            if(sortlist[i] > sortlist[i+1]){
                                int tempval = sortlist[i];
                                sortlist[i] = sortlist[i+1];
                                sortlist[i+1] = tempval;
                                flag = true;
                            }
                        }
                    }
                    cout << "List:" << endl;
                    for(int i = 0; i < listsize; i++) cout << sortlist[i] << " " << endl;
                }
                else if(opt == 7) {
                    string chooser = "";
                    cout << "Would you like to check if some text is a palindrome or if a number is a palindrome "; cin >> chooser;
                    if(chooser == "number"){
                    int a = 0;
                    cout << "Input the number ";cin >> a;
                    int b = 0, n = a;
                    while(a > 0){
                        b *= 10;
                        b += a % 10;
                        a /= 10;
                    }
                    if(b == n) cout << "Your number is a palindrome!" << endl;
                    else cout << "Your number is not a palindrome!" << endl;
                }
                    else if(chooser == "text"){
                        string a;
                        cout << "Input your text: ";
                        cin >> a;

                        int stringlen = a.length();
                        bool isPalindrome = true;

                        for (int i = 0; i < stringlen / 2; i++) {
                            if (a[i] != a[stringlen - i - 1]) {
                                isPalindrome = false;
                                break;
                            }
                        }

                        if (isPalindrome) {
                            cout << "Your text is a palindrome!" << endl;
                        } else {
                            cout << "Your text is not a palindrome!" << endl;
                        }
                    }
                    else cout << "Not a valid option!" << endl;

                }
                else if(opt == 8) {
                    string yourtext = "";
                    int words = 0;
                    int numbers = 0;
                    int letters = 0;
                    int specs = 0;
                    cout << "Enter your text ";
                    cin.ignore();
                    getline(cin, yourtext);
                    int textlen = yourtext.length();
                    for(int i = 0;i < textlen; i++){
                        if(isspace(yourtext[i]))words++ ;
                        if(isdigit(yourtext[i]))numbers++ ;
                        if(isalpha(yourtext[i]))letters++ ;
                        if(!isspace(yourtext[i]) && !isalnum(yourtext[i]))specs++ ;
                    }
                    cout << "There are " << words + 1 << " words in your text" << endl;
                    cout << "There are " << numbers << " numbers in your text"<< endl;
                    cout << "There are " << letters << " letters in your text"<< endl;
                    cout << "There are " << specs << " special charachters in your text"<< endl;
                }
                else if(opt == 0) {return 0;}
                else cout << "Wrong option selected" <<endl;
            }
        }
        else if(auth(in_user, in_pass)){
            int uid = user_id(in_user);
            in_pass = "";
            int opt;
            cout << "[==============================================================]" <<endl;
            cout << "SYSTEM_MESSAGE: Succesfully logged in as user [" << in_user << "]" <<endl;
            while(true){
                cout << "1. Log Out" <<endl;
                cout << "2. Change Username" <<endl;
                cout << "3. Change Password" <<endl;
                cout << "4. Sort Array" <<endl;
                cout << "5. Palindrome Test (int, string)" <<endl;      
                cout << "6. Text Statistics" <<endl;
                cout << "0. Exit" <<endl;
                cout << "Select option: "; cin >> opt;
                if(opt == 1) {break;}
                else if(opt == 2) {
                    string newuser = "";
                    cout << "New username "; cin >> newuser;
                    user[uid] = newuser;
                }
                else if(opt == 3) {
                    string newpass = "";
                    cout << "New password "; cin >> newpass;
                    pass[uid] = newpass;
                }
                else if(opt == 4) {
                    int listsize = 0;
                    cout << "Enter your list length "; cin >> listsize;
                    int sortlist[listsize] = {};
                    for(int i = 0;i < listsize;i++){
                        int tempval = 0;
                        cout << "Enter value "; cin >> tempval;
                        sortlist[i] = tempval;
                    }
                    bool flag = true;
                    while(flag){
                        flag = false;
                        for(int i = 0;i < listsize - 1; i++){
                            if(sortlist[i] > sortlist[i+1]){
                                int tempval = sortlist[i];
                                sortlist[i] = sortlist[i+1];
                                sortlist[i+1] = tempval;
                                flag = true;
                            }
                        }
                    }
                    cout << "List:" << endl;
                    for(int i = 0; i < listsize; i++) cout << sortlist[i] << " " << endl;
                }
                else if(opt == 5) {
                    string chooser = "";
                    cout << "Would you like to check if some text is a palindrome or if a number is a palindrome "; cin >> chooser;
                    if(chooser == "number"){
                    int a = 0;
                    cout << "Input the number ";cin >> a;
                    int b = 0, n = a;
                    while(a > 0){
                        b *= 10;
                        b += a % 10;
                        a /= 10;
                    }
                    if(b == n) cout << "Your number is a palindrome!" << endl;
                    else cout << "Your number is not a palindrome!" << endl;
                }
                    else if(chooser == "text"){
                        string a;
                        cout << "Input your text: ";
                        cin >> a;

                        int stringlen = a.length();
                        bool isPalindrome = true;

                        for (int i = 0; i < stringlen / 2; i++) {
                            if (a[i] != a[stringlen - i - 1]) {
                                isPalindrome = false;
                                break;
                            }
                        }

                        if (isPalindrome) {
                            cout << "Your text is a palindrome!" << endl;
                        } else {
                            cout << "Your text is not a palindrome!" << endl;
                        }
                    }
                    else cout << "Not a valid option!" << endl;
                }
                else if(opt == 6) {
                    string yourtext = "";
                    int words = 0;
                    int numbers = 0;
                    int letters = 0;
                    int specs = 0;
                    cout << "Enter your text ";
                    cin.ignore();
                    getline(cin, yourtext);
                    int textlen = yourtext.length();
                    for(int i = 0;i < textlen; i++){
                        if(isspace(yourtext[i]))words++ ;
                        if(isdigit(yourtext[i]))numbers++ ;
                        if(isalpha(yourtext[i]))letters++ ;
                        if(!isspace(yourtext[i]) && !isalnum(yourtext[i]))specs++ ;
                    }
                    cout << "There are " << words + 1 << " words in your text" << endl;
                    cout << "There are " << numbers << " numbers in your text"<< endl;
                    cout << "There are " << letters << " letters in your text"<< endl;
                    cout << "There are " << specs << " special charachters in your text"<< endl;
                }
                else if(opt == 0) {return 0;}
                else cout << "Wrong option selected" <<endl;
            }
        }
    }
}
