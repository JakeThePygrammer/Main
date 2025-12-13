#include <iostream>
using namespace std;
class Avtomobil{
    private:
    string marka;
    string model;
    int godina;
    public:
    void vnesi(string marka1, string model1, int godina1){
        marka = marka1;
        model = model1;
        godina = godina1;
    };
    void pecati(){
        cout << "Marka : " << marka << " Model : " << model << " Godina : " << godina << endl;
    };
    int starost(int tekovnaGodina){
        return tekovnaGodina - godina;
    }
};

int main(){
    Avtomobil a1;
    string marka2, model2;
    int godina2, tekgod;
    cout << "Vnesi marka, model, godina na proizvodstvo i tekovna godina : " << endl;
    cin >> marka2 >> model2 >> godina2 >> tekgod;
    a1.vnesi(marka2, model2, godina2);
    a1.pecati();
    cout << "Starost : " << a1.starost(tekgod) << endl;
}