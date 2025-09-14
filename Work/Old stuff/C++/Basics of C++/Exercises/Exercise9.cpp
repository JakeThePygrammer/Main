#include <iostream>
#include <string>
using namespace std;

int main() {
	string recen;
	string underrecen;
	cout << "Input : ";
	getline(cin, recen);
	int lenrec;
	cout << recen << endl;
	lenrec = recen.length();
	for (int i = 0; i < lenrec; i++) {
		if (isdigit(recen[i])) cout << "*";
		else if (isupper(recen[i])) cout << "U";
		else if (isspace(recen[i])) cout << "-";
		else if (islower(recen[i])) cout << "L";
		else cout << "?";

	}
}
