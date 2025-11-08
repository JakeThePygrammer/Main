#include <iostream>
using namespace std;

struct imeprezime {
    string ime;
    string prezime;
};

struct Student {
    imeprezime imeprezime1;
    int index;
    int godinaStudii;

    void replacer(string ime1, string prezime1, int index1, int godinaStudii1) {
        imeprezime1.ime = ime1;
        imeprezime1.prezime = prezime1;
        index = index1;
        godinaStudii = godinaStudii1;
    }

    void printer() {
        cout << "Index of student: " << index << endl;
        cout << "Name of student: " << imeprezime1.ime << " " << imeprezime1.prezime << endl;
        cout << "Years studying: " << godinaStudii << endl;
    }
};

int main() {
    Student student1,student2,student3;
    student1.replacer("Jakov", "Nestorovski", 12905, 3);
    student1.printer();
    student2.replacer("Zaklina", "Popovska", 12511, 2);
    student2.printer();
    student3 = {{"Jovana", "Zarki"},15812,1};
    cout<<"Name "<<student3.imeprezime1.ime<<" Index "<<student3.index<<endl;
}