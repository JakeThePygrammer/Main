#include <iostream>
#include <string>
using namespace std;

class Book{
private:
    string booktitle;
    string author;
    int year;
public:
    void Enterer(string bbooktitle, string bauthor, int byear){
        booktitle = bbooktitle;
        author = bauthor;
        year = byear;
    };
    void Output(){
        cout <<"\n"<< booktitle << " by " << author << ", " << year << endl;
    };
};

int main(){
    string bookname, authorname;
    int yearout;
    cout << "Name of the book : ";
    getline(cin, bookname);
    cout << "Name of the author : ";
    getline(cin, authorname);
    cout << "Year the book came out : "; cin >> yearout;
    Book b1;
    b1.Enterer(bookname,authorname,yearout);
    b1.Output();
}