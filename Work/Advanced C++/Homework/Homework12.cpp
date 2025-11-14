#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    string surname;
    int student_number;
    
public:

    Student() {
        name = "";
        surname = "";
        student_number = 0;
    }

    Student(string names, string surnames, int student_numbers) {
        name = names;
        surname = surnames;
        student_number = student_numbers;
    }

    void replacer(string names, string surnames, int student_numbers) {
        name = names;
        surname = surnames;
        student_number = student_numbers;
    }
};

class Grades {
private:
    int Macedonian;
    int English;
    int Foreignlanguage;
    int Math;
    int Biology;
    int PE;
    int Geography;
    int History;
    int Art;

public:

    Grades() {
        Macedonian = 0;
        English = 0;
        Foreignlanguage = 0;
        Math = 0;
        Biology = 0;
        PE = 0;
        Geography = 0;
        History = 0;
        Art = 0;
    }

    Grades(int Macedonians, int Englishs, int Foreings, int Maths,
           int Biologys, int PEs, int Geographies, int Historys, int Arts) {
        Macedonian = Macedonians;
        English = Englishs;
        Foreignlanguage = Foreings;
        Math = Maths;
        Biology = Biologys;
        PE = PEs;
        Geography = Geographies;
        History = Historys;
        Art = Arts;
    }

    void replacer2(int Macedonians, int Englishs, int Foreings, int Maths,
                   int Biologys, int PEs, int Geographies, int Historys, int Arts) {
        Macedonian = Macedonians;
        English = Englishs;
        Foreignlanguage = Foreings;
        Math = Maths;
        Biology = Biologys;
        PE = PEs;
        Geography = Geographies;
        History = Historys;
        Art = Arts;
    }
};

int main() {
    int n;
    cout << "Enter the number of students you want to enter: ";
    cin >> n;
    cin.ignore();

    Student students[n];
    Grades gradeses[n];

    for (int i = 0; i < n; i++) {
        string names, surnames;
        int Macedonians, Englishs, Foreings, Maths, Biologys, PEs, Geographies, Historys, Arts;
        int student_numbers;

        cout << "Enter the name for student " << i + 1 << ": ";
        cin >> names;

        cout << "Enter the surname for student " << i + 1 << ": ";
        cin >> surnames;

        cout << "Enter the Macedonian grade for student " << i + 1 << ": ";
        cin >> Macedonians;

        cout << "Enter the English grade for student " << i + 1 << ": ";
        cin >> Englishs;

        cout << "Enter the foreign language grade for student " << i + 1 << ": ";
        cin >> Foreings;

        cout << "Enter the Math grade for student " << i + 1 << ": ";
        cin >> Maths;

        cout << "Enter the Biology grade for student " << i + 1 << ": ";
        cin >> Biologys;

        cout << "Enter the PE grade for student " << i + 1 << ": ";
        cin >> PEs;

        cout << "Enter the Geography grade for student " << i + 1 << ": ";
        cin >> Geographies;

        cout << "Enter the History grade for student " << i + 1 << ": ";
        cin >> Historys;

        cout << "Enter the Art grade for student " << i + 1 << ": ";
        cin >> Arts;
        
        student_numbers = i + 1; 

        gradeses[i].replacer2(Macedonians, Englishs, Foreings, Maths, Biologys, PEs, Geographies, Historys, Arts);

        students[i].replacer(names, surnames, student_numbers);
    }

    return 0;
}
