#include <iostream>
#include <string>
using namespace std;

class Book {
private:
    string bookname;
    string author;
    int ISBN;
    int price;
public:
    Book(){
        bookname = "";
        author = "";
        ISBN = 0;
        price = 0;
    }
    void replacer(string bookname1, string author1, int ISBN1, int price1) {
        bookname = bookname1;
        author = author1;
        ISBN = ISBN1;
        price = price1;
    }

    void printer() {
        cout << "ISBN: " << ISBN << endl;
        cout << bookname << " by " << author << endl;
        cout << "Price: " << price << endl;
    }

};

int main() {
    Book books;
    string booknames, authors;
    int ISBNs, prices;
    cout << "Enter the name for the book " << ": ";
    getline(cin, booknames);

    cout << "Enter the author for the book " << ": ";
    getline(cin, authors);

    cout << "Enter the price for the book " << ": ";
    cin >> prices;

    cout << "Enter the ISBN for the book " << ": ";
    cin >> ISBNs;
    cin.ignore();
    
    books.replacer(booknames, authors, ISBNs, prices);
    books.printer();
    return 0;
}