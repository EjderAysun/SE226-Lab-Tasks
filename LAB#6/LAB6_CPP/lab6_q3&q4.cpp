#include <iostream>
#include <math.h> 
using namespace std;

// question 3 //
float computeSum(int n) {

    /**
    Computes the sum of the series ∑(-1)^(k+1)/k from k=1 to n
    
    The upper limit of the sum (non-negative integer).
    The program prompts the user to enter the value of n,
    and then calls the function `computeSum` to compute the sum.
    The function is implemented using recursion.
    The base case is when n <= 0, in which case the function returns 0.
    Otherwise, it calls itself with the argument n-1 and adds the current term to the result.

    @param
        n: int

    @return 
        The computed sum.

    @returnType
        float

    @example
        >>> computeSum(3)
        0.8333333333333333
        >>> computeSum(100)
        0.688172179310195
        >>> computeSum(0)
        0
        >>> computeSum(-35)
        0
    */

    if (n > 0) {
        return pow((-1), (n + 1)) / n + computeSum(n - 1);
    }
    return 0;
}

// question 4 //
float computeSum() {
    int n;
    cout<<"Please enter n as an integer: ";
    cin>>n;

    if (n > 0) {
        return pow((-1), (n + 1)) / n + computeSum(n - 1);
    }
    return 0;
}

// test //
int main() {

    // question 3 test //
    int n;
    cout<<"Please enter n as an integer: ";
    cin>>n;
    cout<<"Sum: "<<computeSum(n)<<endl;

    // question 4 test //
    float sum = computeSum();
    cout<<"Sum: "<<sum<<endl;
    return 0;
}