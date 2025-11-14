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

    books.bookname = booknames;
    books.price = prices;
    books.author = authors;
    books.ISBN = ISBNs;
    cout << books.bookname << " by " << books.author << " ISBN : " << books.ISBN << " Price : " << books.price << endl;
    return 0;
}