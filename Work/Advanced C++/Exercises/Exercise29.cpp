#include <iostream>
using namespace std;
void greeting(string name, int age){
    cout << "Hello " << name << "! " << "You're "<< age <<" years old!" << endl;

}
int main(){
    string name;
    int age;
    cout << "Enter your name : ";cin >> name;
    cout << "Enter your age : ";cin >> age;
    greeting(name,age);
}