#include <iostream>
using namespace std;

bool palindrom(int a) {
	int b = 0, n = a;

	while (a > 0) {
		b *= 10;
		b += a % 10;
		a /= 10;
	}
	return b == n;

}
int main() {
	long long int n = 99999999999999999999999999999999999;
	long long int brojac = 1;
	for (long long int i = 0; i < n; i++) {
		if (palindrom(i)) {
			cout << "Palindrome " << brojac << " : " << i << endl;
			brojac++;
		}
	}
}
