#include <iostream>
using namespace std;

int main() {
	int i = 0;
	int broj[26];
	while (i < 26) {
		broj[i] = 0;
		i++;
	}
	string test = "ovde ima test recenica, site sme pospani deka e sabota nasabajle. mi treba kafe.";
	int golemina = 0;
	while (test[golemina] != '\0') golemina++;
	i = 0;
	int input;
	while (i < golemina) {
		if ((test[i] - 97) >= 0) {
			broj[test[i] - 97]++;
		}
		i++;
	}
	i = 0;
	while (i < 26) {
		cout << (char)(97 + i) << ": " << broj[i] << endl;
		i++;
	}
}