#include <iostream>
using namespace std;

//This is the way that matrixes(2D lists) are created

int main() {
    int red, kol;
    cout << "Enter the amount of rows in the matrix: ";
    cin >> red;
    cout << "Enter the amount of columns in the matrix: ";
    cin >> kol;
    int matrix[red][kol];
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << "Enter value [" << i << "][" << j << "]: ";
            cin >> matrix[i][j];
        }
    }
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << matrix[i][j] << " ";
        }
        cout<<endl;
    }
}

//This is how to only have diagonal values entered

int main() {
    int red, kol;
    cout << "Enter the amount of rows in the matrix: ";
    cin >> red;
    cout << "Enter the amount of columns in the matrix: ";
    cin >> kol;
    int matrix[red][kol];
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
        if(i==j){
            cout << "Enter value [" << i << "][" << j << "]: ";
            cin >> matrix[i][j];
        }
        else{
            matrix[i][j]=0;
        }
        }
    }
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << matrix[i][j] << " ";
        }
        cout<<endl;
    }


//For upper and lower triangle

//Upper triangle

for(int i=0; i < red;i++){
    for(int j=i;j<kol;j++){
        Q[i],[j]
        }
}

//Lower triangle

for(int i=0;i<red;i++){
    for(int j=0; j<=i;j++){
        Q[i][j]
    }
}
}


//Combining 2 matrixes

int main() {
    int red, kol;
    cout << "Enter the amount of rows in the matrixes: ";
    cin >> red;
    cout << "Enter the amount of columns in the matrixes: ";
    cin >> kol;
    int matrix[red][kol];
    int matrix1[red][kol];
    int matrixcol[red][kol];
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << "Enter value [" << i << "][" << j << "] for matrix 1: ";
            cin >> matrix[i][j];
            cout << "Enter value [" << i << "][" << j << "] for matrix 2: ";
            cin >> matrix1[i][j];
            matrixcol[i][j] = matrix[i][j]+matrix1[i][j];
        }
    }
    for (int i = 0; i < red; i++) {
        for (int j = 0; j < kol; j++) {
            cout << matrixcol[i][j] << " ";
        }
        cout<<endl;
    }


//Symmetric matrixes

int A[3][3] = 
{
    {1,4,0},
    {4,-1,1},
    {0,1,0}
};

bool isSymmetric = true;
for(int i=0;i<3;i++){
    for(int j=0;j<3;j++){
        if(A[i][j]!=A[j][i]){
            isSymmetric = false;
            break;
        }
    }
}
}
//Multiplying matrixes(transpondent matrixes)

int main(){
    int rows1=2, columns1 = 3, rows2=3, columns2=2;
    int A[rows1][columns1] = {
        {1,2,3},
        {4,5,6}
    };
    int B[rows2][columns2] = {
        {7,8},
        {9,10},
        {11,12}
    };
    int C[2][2] = {
        {0,0},
        {0,0}
    };
    for(int i=0;i<rows1;i++){
        for(int j=0;j<columns2;j++){
            for(int k=0;k<columns1;k++){
                C[i][j] += A[i][k] * B[k][j];
                //cout << i << " - i " << j << " - j " << k << " - k " << endl;
                //Use to visualize the for cycles
            }
        }
    }
    for(int i=0;i<rows1;i++){
        for(int j=0;j<columns2;j++){
            cout<<C[i][j]<<" ";
        }
        cout<<endl;
    }


//Switching rows in a matrix

int A[3][3] = 
{
    {1,1,1},
    {2,2,2},
    {3,3,3}
};
for(int i=0;i<3;i++){
    int temp = A[0][i];
    A[0][i] = A[2][i];
    A[2][i] = temp;
}

//Switching columns in a matrix 
int A[3][3] = 
{
    {1,1,1},
    {2,2,2},
    {3,3,3}
};
for(int i=0;i<3;i++){
    int temp = A[i][0];
    A[i][0] = A[i][2];
    A[i][2] = temp;
}
}

#include <fstream>
//REMEMBER-READING WITH IFSTREAM WRITING WITH OFSTREAM
//Reading with ifstream
int main(){
    ifstream vlez;
    vlez.open("HelloWorld.txt");
    if(!vlez)
        cout<<"The file doesnt exist!"<<endl;
    else
        cout<<"Successfully opened file.";
    vlez.close();
    return 0;
}
//Writing with ofstream
int main(){
    ofstream izlez;
    izlez.open("HelloWorld.txt");
    izlez.close();
    return 0;
}

//Reading in file
int main(){
    ifstream vlez;
    vlez.open("HelloWorld.txt");
    int n;
    string s;
    vlez>>n>>s; //to read
    cout<<s<<endl;
    vlez.close();
    return 0;
}

//Writing to file(deletes whole file data unless during open if you add "ios::app" 'vlez.open("HelloWorld.txt", ios::app'))
//Ofstream creates files if they don't exist

int main(){
    ofstream vlez;
    vlez.open("HelloWorld.txt");
    vlez<<1; //to write
    vlez<<" Hello World"<<endl;
    vlez.close();
    return 0;
}

//Writing multiple

int main(){
    ofstream vlez;
    vlez.open("HelloWorld.txt");
    string meseci[12] = {"januari","fevruari","mart","april","maj","juni","juli","avgust","septemvri","oktomvri","noemvri","dekemvri"};
    for(int i=0;i<=11;i++)
        vlez<<meseci[i]<<endl;
    vlez.close();
    return 0;
}

/*Fstream is to choose with ios::in and ios::out instead of ifstream and ofstream, to divide multiple use |.

ios::-tags
ios::in-to read
ios::out-to wrote
ios::app-to append
ios::ate-finds end
ios::nocreate-only opens file
ios:noreplace-only creates file
*/
int main(){
    fstream file;
    file.open("HelloWorld.txt",ios::in);
    int a,b;
    file>>a>>b;
    file.close();
    cout<<"a + b = " << a+b;
    file.open("HelloWorld.txt",ios::out|ios::app);
    file<<endl;
    file<<a+b<<endl;
    file.close();
    return 0;

}

//Functions to use

int main(){
    ifstream dat("HelloWorld.txt");
    int sum = 0;
    if(dat.is_open() == false){
        cout<<"The file isn't open!";
        return 0;
    }
    while(dat.eof() == false){
        int temp;
        dat >> temp;

    if(dat.fail() == true){
        cout<<"The data given was not a whole number!";
        return 0;
    }
    else
        sum+=temp;
    }

    cout<<"The sum is "<<sum<<endl;
    return 0;
}

//How to transfer data from one file to another

#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream dava("izlez.txt");
    ifstream zima("vlez.txt");
    string tempval;
    while (!zima.eof()) {
        getline(zima, tempval);
        dava << tempval << endl;
    }
    dava.close();
    zima.close();
    ifstream readtext("izlez.txt");
    string lines;
    while (!readtext.eof()) {
        getline(readtext, lines);
        cout << lines << endl;
    }
    readtext.close();
    return 0;
}
//Functions are like seperate int mains, we can call them like predefined functions
int Pogolem(int broj1, int broj2){
    if(broj1 > broj2)return broj1;
    else return broj2;
}

int main(){
    cout<<Pogolem(1,2);
    int a = Pogolem(6,12);
    return 0;
}

/*cmath functions
sqrt(x,y)-Square root
pow(x,y)-To the power of
*/

//Getline allows for spaces in input
//Cin is for the text input, tempval is for the text itself
int main() {
    ofstream dava("izlez.txt");
    string tempval;
    int amountoflines;
    cout<<"Enter the amount of lines you want to write to the file: ";
    cin>>amountoflines;
    for(int i=0;i<amountoflines;i++){
        cout<<"Enter name, surname and phone number for line "<<i+1<<": ";
        getline(cin, tempval);
        dava<<tempval<<endl;
    }
    dava.close();
    return 0;
}


//OOP(object oriented programming)
//Defining a structure
struct imeprezime {
    string ime;
    string prezime;
};

struct Student {
    //Taking from another structure
    imeprezime imeprezime1;
    int index;
    int godinaStudii;

    void replacer(string ime1, string prezime1, int index1, int godinaStudii1) {
        //Using the attributes from another structure
        imeprezime1.ime = ime1;
        imeprezime1.prezime = prezime1;
        index = index1;
        godinaStudii = godinaStudii1;
    }

    void printer() {
        cout << "Index of student: " << index << endl;
        cout << "Name of student: " << imeprezime1.ime << " " << imeprezime1.prezime << endl;
        cout << "Years studying: " << godinaStudii << endl;
    }
};

int main() {
    Student student1,student2,student3;
    //With method
    student1.replacer("Jakov", "Nestorovski", 12905, 3);
    student1.printer();
    student2.replacer("Zaklina", "Popovska", 12511, 2);
    student2.printer();
    //Without method
    student3 = {{"Jovana", "Zarki"},15812,1};
    cout<<"Name "<<student3.imeprezime1.ime<<" Index "<<student3.index<<endl;
}

// Differences between struct and class:

struct PersonS {
        //always public
    string nameandsurname;
    int age;
};

class PersonC {
private://private by defaut
    string nameandsurname;
    int age;
    /*
    Public - can be read without functions                                       Yes Yes
    Protected - can't be read without functions and can be used in other classes  No Yes
    Private - can't be read without functions and can't be used in other classes  No No
    */

public:
    // Constructor(can have none, some or all of the variables)
    PersonC(string name, int a) : nameandsurname(name), age(a) {}

    // Getters
    string getNameAndSurname() {
        return nameandsurname;
    }

    int getAge() {
        return age;
    }

    // Setters
    void setNameAndSurname(string name) {
        nameandsurname = name;
    }

    void setAge(int a) {
        age = a;
    }
};

int main() {
    // Using struct
    PersonS person1;
    person1.age = 20;
    person1.nameandsurname = "Jakov Nestorovski";

    // Using class
    PersonC person2("Jovan Jovanovski", 22);

    cout << "Struct person: " << person1.nameandsurname/*Can be gotten directly*/ << ", " << person1.age << " years old" << endl;
    cout << "Class person: " << person2.getNameAndSurname()/*Only can be get with functions*/ << ", " << person2.getAge() << " years old" << endl;

    return 0;
}

//REMEMBER - USE PROTECTED WHEN MAKING CHILD ATTRIBUTES WITH CLASSES!!!