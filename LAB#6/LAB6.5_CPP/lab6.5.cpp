#include <iostream>
#include <list>
#include <algorithm>
#include <set>
#include <numeric>
#include <sstream>

using namespace std;

// helper methods //
template <typename T>
void printList(list<T> list) {
    stringstream ss;
    ss << "{";
    for (const T& item : list) {
        ss << item << ", ";
    }
    string result = ss.str();
    int ssSize = result.size();
    if(ssSize > 2) result.erase(ssSize - 2);
    result += "}";
    cout << result << endl;
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

string extractMultipleLetters(string sortedWord) {
    set<char> charSet(sortedWord.begin(), sortedWord.end());
    return accumulate(charSet.begin(), charSet.end(), string());
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
// Any string containing just one letter is by default a palindrome.
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

// task 3 //
// The Sieve of Eratosthenes is valid for consecutive numbers from 2 to n.
list<int> sieveOfEratosthenes(list<int> numList) {
    list<int> primes = numList;
    primes.sort();
    int p = 2;
    int size = primes.size() - 1;
    while(p * p <= size) {
        list<int> primesSubList(next(primes.begin(), p - 1), primes.end());
        for(int item : primesSubList) {
            if (item % p == 0) primes.remove(item);
        }
        p += 1;
    }
    return primes;
}

// task 4 //
list<string> anagrams(string word, list<string> wordList) {
    list<string> anagramList;
    word = extractMultipleLetters(toLower(word));
    for (int i = 0; i <= wordList.size()-1; i++) {
        string extractedMultipleLettersWord = extractMultipleLetters(toLower(*next(wordList.begin(), i)));
        if(word == extractedMultipleLettersWord) {
            anagramList.push_back(*next(wordList.begin(), i));
        }
    }
    return anagramList;
}

int main() {
    // task 1 //
    list<int> list1 = {1,2,3,4,5,6};
    list<int> list2 = {3,4,5,7,8,9,0};
    printList(findCommonElements1(list1, list2));
    // or
    printList(findCommonElements2(list1, list2));

    // task 2 //
    list<string> strings = {"rotator", "wow", "noon", "civic", "level", "Bob", "Ross", "Tenet", "a"};
    printList(palindrom1(strings));
    // or
    printList(palindrom2(strings));

    // task 3 //
    list<int> numList = {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,25,26,27,28,29,30};
    printList(sieveOfEratosthenes(numList));

    // task 4 //
    list<string> wordList = {"enlists", "google", "inlets", "banana"};
    string word = "listen";
    printList(anagrams(word, wordList));
    
    return 0;
}