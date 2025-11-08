#include <iostream>
using namespace std;

struct PersonS {
    string nameandsurname;
    int age;
};

class PersonC {
private:
    string nameandsurname;
    int age;

public:
    // Constructor
    PersonC(string name, int a) : nameandsurname(name), age(a) {}

    // Getters
    string getNameAndSurname() {
        return nameandsurname;
    }

    int getAge() {
        return age;
    }

    // Setters
    void setNameAndSurname(string name) {
        nameandsurname = name;
    }

    void setAge(int a) {
        age = a;
    }
};

int main() {
    // Using struct
    PersonS person1;
    person1.age = 20;
    person1.nameandsurname = "Jakov Nestorovski";

    // Using class
    PersonC person2("Jovan Jovanovski", 22);

    cout << "Struct person: " << person1.nameandsurname << ", " << person1.age << " years old" << endl;
    cout << "Class person: " << person2.getNameAndSurname() << ", " << person2.getAge() << " years old" << endl;

    return 0;
}
