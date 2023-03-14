#include <iostream>
using namespace std;

int main() {

    string name, surname;
    float lab_grade, midterm_grade, final_grade;

    cout<<"Please do not leave any spaces when entering.";

    cout<<"What is your name? ";
    cin>>name;
    cout<<"What is yoru surname? ";
    cin>>surname;

    // When using the "cin" method it only takes the value up to the first space of the first line.
    // We can solve this problem as "getline(cin, name)".
    // However, since we were told not to go beyond what was explained in the lesson while solving laboratory tasks,
    // I first took only the name and then only the surname.
    // After that, I combined the name and surname I got from the user and printed it on the screen.

    cout<<"What is your lab grade? ";
    cin>>lab_grade;
    cout<<"What is your midterm grade? ";
    cin>>midterm_grade;
    cout<<"What is your final grade? ";
    cin>>final_grade;



    float last_score;
    last_score = (lab_grade * 25 / 100) + (midterm_grade * 35 / 100) + (final_grade * 40 / 100);

    cout<<"Name: "<<name + " " + surname<<endl;
    //cout<<name + " " + surname<<endl;
    cout<<"Lab: "<<lab_grade<<endl;
    // cout<<lab_grade<<endl;
    cout<<"Midterm: "<<midterm_grade<<endl;
    // cout<<midterm_grade<<endl;
    cout<<"Final: "<<final_grade<<endl;
    // cout<<final_grade<<endl;
    cout<<"Last score: "<<last_score<<endl;
    // cout<<last_score<<endl;

    // Results can be printed on the screen in two different ways and both methods are the same, and easier to read as above.

    return 0;
}