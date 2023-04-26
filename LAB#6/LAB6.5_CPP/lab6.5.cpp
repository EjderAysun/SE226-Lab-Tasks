#include <iostream>
#include <list>
#include <algorithm>
#include <typeinfo>
#include <string>

using namespace std;

// helper methods //
void printIntList(list<int> list) {
    string result = "{";
    for (int it : list) {
        result += to_string(it) + ", ";
    }
    // result.erase(result.size()-2);
    result += "}";
    cout<<result<<endl;
}

void printStrList(list<string> list) {
    string result = "{";
    for (string it : list) {
        result += it + ", ";
    }
    // result.erase(result.size()-2);
    result += "}";
    cout<<result<<endl;
}

string toLower(string str) {
    string result;
    for (char c : str) {
        result += std::tolower(c);
    }
    return result;
}

string reverse(string str) {
    int n = str.length();
    for (int i = 0; i < n / 2; i++) {
        swap(str[i], str[n - i - 1]);
    }
    return str;
}

// task 1 //
list<int> findCommonElements1(list<int> aList1, list<int> aList2) {
    list<int> commonElements;
    for(int i : aList1) {
        for(int j : aList2) {
            if(i == j) commonElements.push_back(i);
        }
    }
    return commonElements;
}
// or
list<int> findCommonElements2(list<int> aList1, list<int> aList2) {
    list<int> intersection;
    set_intersection(aList1.begin(), aList1.end(), aList2.begin(), aList2.end(), back_inserter(intersection));
    return intersection;
}

// task 2 //
list<string> palindrom1(list<string> strings) {
    list<string> returnList;
    for(string i : strings) {
        string word = toLower(i);
        int l = i.size();
        int indexCons = int(l/2);
        if((l%2==1 && word.substr(0, indexCons) == reverse(word.substr(indexCons+1, l)) || (l%2==0 && word.substr(0, indexCons) == reverse(word.substr(indexCons, l)))))
            returnList.push_back(i);
    }
    return returnList;
}
// or
list<string> palindrom2(list<string> strings) {
    list<string> returnList;
    for (string str : strings) {
        string strLower = toLower(str);
        string strLowerReverse = reverse(strLower);
        if(strLower == strLowerReverse) returnList.push_back(str);
    }
    return returnList;
}

int main() {
    // task 1 //
    list<int> list1 = {1,2,3,4,5,6};
    list<int> list2 = {3,4,5,7,8,9,0};
    printIntList(findCommonElements1(list1, list2));
    // or
    printIntList(findCommonElements2(list1, list2));

    // task 2 //
    list<string> strings = {"rotator", "wow", "noon", "civic", "level", "Bob", "Ross", "Tenet", "a"};
    printStrList(palindrom1(strings));
    printStrList(palindrom2(strings));
}