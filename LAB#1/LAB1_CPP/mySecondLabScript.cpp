#include <iostream>
using namespace std;

int main() {

    int var1, var2;

    cout<<"Please do not leave any spaces when entering.";

    cout<<"Please enter var1: ";
    cin>>var1;
    cout<<"Please enter var2: ";
    cin>>var2;

    int sum, diff, prod;

    sum = var1 + var2;
    diff = var1 - var2;
    prod = var1 * var2;

    cout<<"var1: "<<var1<<endl;
    // cout<<var1<<endl;
    cout<<"var2: "<<var2<<endl;
    // cout<<var2<<endl;
    cout<<"sum (var1 + var2): "<<sum<<endl;
    // cout<<sum<<endl;
    cout<<"diff (var1 - var2): "<<diff<<endl;
    //cout<<diff<<endl;
    cout<<"prod: (var1 * var2): "<<prod<<endl;
    // cout<<prod<<endl;

    // Results can be printed on the screen in two different ways and both methods are the same, and easier to read as above.

    return 0;
}