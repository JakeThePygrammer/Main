#include <iostream>
using namespace std;

int main() {
	string test = "Hello world! Hi,my name is CLW93.";
	int i = 0;
	int words = 0;
	int a = test.length();
	for (i = 0; i < a; i++) {
		if (test[i] != ' ' && test[i - 1] == ' ') words++;
	}
	cout << "The number of words is: " << words + 1 << endl;
}
