#include <iostream>
using namespace std;

bool palindromnum(int a) {
	int b = 0, n = a;

	while (a > 0) {
		b *= 10;
		b += a % 10;
		a /= 10;
	}
	return b == n;

}
bool palindromstring(string a) {
    int stringlength = a.length();
    for (int i = 0; i < stringlength / 2; i++) {
        if (a[i] != a[stringlength - i - 1]) {
            return false;
        }
    }
    return true;
}

int main(){
	if (palindromnum(11)) cout << "Num = true" << endl;	
	else cout << "Num = false" << endl;
    if (palindromstring("racecars")) cout << "String = true" << endl;
	else cout << "String = false" << endl;
}