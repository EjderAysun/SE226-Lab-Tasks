#include <iostream>
using namespace std;

int main() {

    string name, id; // In the context of this question, there is no need to get the id as an integer.

    cout<<"Please do not leave any spaces when entering.";

    cout<<"What is your name?"<<endl;
    cin>>name;
    cout<<"Hello " + name + "."<<endl;
    cout<<"What is your student ID?"<<endl;
    cin>>id;
    cout<<"Your ID is " + id + "."<<endl; 

    return 0;
}