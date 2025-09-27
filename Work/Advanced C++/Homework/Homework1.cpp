#include <iostream>
using namespace std;
int main()
{
    int lengthoflist, offset;
    cout << "Enter the length of the list: "; cin >> lengthoflist;
    int oldlist[lengthoflist], newlist[lengthoflist];
    for(int i = 0; i < lengthoflist; i++){
        cout << "Enter element " << i + 1 << " of the list: ";
        cin >> oldlist[i];
    }
    cout << "Enter the offset: "; cin >> offset;
    for(int i = 0; i < lengthoflist; i++){
        int value = i + offset;
        if(value >= lengthoflist) value -= lengthoflist;
        newlist[value] = oldlist[i];
    }
    cout << "Old list: ";
    for(int i = 0; i < lengthoflist; i++){
        cout << oldlist[i] << " " ;
    }
    cout << endl;
    cout << "New list: ";
    for(int i = 0; i < lengthoflist; i++){
        cout << newlist[i] << " " ;
    }
    cout << endl;
    return 0;
}