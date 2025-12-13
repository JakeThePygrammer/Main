#include <iostream>
using namespace std;
int main()
{
    int lengthoflist;
    cout << "Enter the length of the list: "; cin >> lengthoflist;
    int lists[lengthoflist];
    for(int i = 0; i < lengthoflist; i++){
        cout << "Enter element " << i + 1 << " of the list: ";
        cin >> lists[i];
            }
    for(int i = 0; i < lengthoflist; i++){
        cout << lists[lengthoflist-i-1] << " " ;


}
}
