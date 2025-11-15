#include <iostream>
using namespace std;

class Student {
private:
    string name;
    string surname;
    int grades[3];
    
public:
    void enter() {
        string names, surnames;
        cout << "Enter name : ";
        cin >> names;
        cout << "Enter surname : ";
        cin >> surnames;
        name = names;
        surname = surnames;
        for (int i = 0; i < 3; i++) {
            int tempval = 0;
            cout << "Enter grade " << i+1 << " : "; cin >> tempval;
            grades[i] = tempval;
        }
    }
    float average(){
        float gradeaverage = 0;
        for(int i = 0;i<3;i++){
            gradeaverage += grades[i];
        }
        return gradeaverage/3;
    }
    void print() {
        cout << "Grade average : "<< average() << endl;
        cout << "Name and surname : "<< name << surname << endl;
    }
};
int main(){
    Student s1;
    s1.enter();
    s1.print();
}