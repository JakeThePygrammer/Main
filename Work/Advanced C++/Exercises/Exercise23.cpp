#include <iostream>
#include <string>
using namespace std;

struct Book {
    string bookname;
    string author;
    int ISBN;
    int price;

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
    int n;
    cout << "Enter the number of books you want to enter: ";
    cin >> n;
    cin.ignore();

    Book books[n];

    for (int i = 0; i < n; i++) {
        string bookname, author;
        int ISBN, price;

        cout << "Enter the name for book " << i + 1 << ": ";
        getline(cin, bookname);

        cout << "Enter the author for book " << i + 1 << ": ";
        getline(cin, author);

        cout << "Enter the price for book " << i + 1 << ": ";
        cin >> price;

        cout << "Enter the ISBN for book " << i + 1 << ": ";
        cin >> ISBN;
        cin.ignore();

        books[i].replacer(bookname, author, ISBN, price);
        books[i].printer();
    }

    return 0;
}
