#include <iostream>
using namespace std;

string createMail(string name,string surname, string domain){
    string res = name + "." + surname + "@" + domain;
    return res;
}

int main(){
    cout << createMail("jakov", "nestorovski", "nestorovski.com");
}