#include <iostream>
#include <string>
using namespace std;


bool checkpass(string pass) {
    bool yeslength = false;
    bool yesspec = false;
    bool yesnum = false;
    bool yeshigh = false;
    int highs = 0;
    int passlen = pass.length();
    if (passlen >= 8)yeslength = true;
    for (int i = 0; i < passlen; i++) {
        if (isdigit(pass[i]))yesnum = true;
        if (isupper(pass[i])) highs + 1;
        if (highs >= 2)yeshigh = true;
        if (!isalpha(pass[i]) && !isdigit(pass[i]) && i != passlen - 1)yesspec = true;
        if (yeslength && yeshigh && yesspec && yesnum) return true;
    }
}

string usernameandpassword(string users, string passes, bool newuser) {
    string user[3] = { "Jakov", "Maksim", "ABC" };
    string pass[3] = { "123Jakov", "MaksimPro", "ABC" };
    int userid = -1;
    string changepass;
    string oldpassword;
    string newpassword1;
    string newpassword2;
    string newpasstemp;

    if (newuser) {
        for (int i = 0; i < 3; i++) {
            if (user[i] == "ABC" && pass[i] == "ABC") {
                user[i] = users;
                pass[i] = passes;
                cout << "New user added! Taken user " << i + 1 << "/3" << endl;
                return " ";

            }
        }
    }
    else if (newuser == false) {
        for (int i = 0; i < 3; i++) {
            if (users == user[i]) {
                userid = i;
                break;
            }
        }
    }
    else return "No more user slots available!";

    if (userid != -1 && users == user[userid] && passes == pass[userid]) {
        cout << "Approved!" << endl;
        cout << "Change password?[Y/N]" << endl;
        cin >> changepass;
        if (changepass == "Y") {
            cout << "Old password:" << endl;
            cin >> oldpassword;
            if (oldpassword == pass[userid]) {
                cout << "New password:" << endl;
                cin >> newpassword1;
                cout << "Repeat new password:" << endl;
                cin >> newpassword2;
                if (newpassword1 == newpassword2 && checkpass(newpassword1) && checkpass(newpassword2)) {
                    pass[userid] = newpassword1;
                    cout << "Reauthenticate with just your password!" << endl;
                    cout << "Enter changed password" << endl;
                    cin >> newpasstemp;
                    if (pass[userid] == newpasstemp) {
                        return "Password change verified!";
                    }
                }
                else {
                    return "Passwords do not match or do not meet safety requirements!";
                }
            }
            else {
                return "Incorrect old password!";
            }
        }
        else {
            return "Successful login!";
        }
    }
    else {
        return "Denied!";
    }
}

int main() {
    string userinput;
    string passinput;
    bool newuserinput;
    cout << "Are you a new user? [0 = No/1 = Yes]: ";
    cin >> newuserinput;
    cout << "Enter username: ";
    cin >> userinput;
    cout << "Enter password: ";
    cin >> passinput;
    cout << usernameandpassword(userinput, passinput, newuserinput) << endl;
}


