# task 1 #

def findCommonElements1(aList1, aList2):
    return [i for i in aList1 if i in aList2]
# or
def findCommonElements2(aList1, aList2):
    return list(set(aList1).intersection(set(aList2)))

# task 2 #
# Any string containing just one letter is by default a palindrome.
def palindrom1(strings):
    returnList = []
    for i in strings:
        word = i.lower()
        l = len(i)
        indexCons = int(l/2)
        if((l%2==1 and word[0:indexCons] == word[l:indexCons:-1]) or (l%2==0 and word[0:indexCons] == word[l:indexCons-1:-1])):
            returnList.append(i)
    return returnList
# or #
def palindrom2(strings):
    return [str for str in strings if str.lower() == str[::-1].lower()]

# task 3 #
# The Sieve of Eratosthenes is valid for consecutive numbers from 2 to n.
def sieveOfEratosthenes(num_list):
    primes = num_list.copy()
    primes.sort()
    p = 2
    length = len(primes) - 1
    while(p * p <= length):
        for item in primes[p-1:len(primes)]:
            if item % p == 0:
                primes.remove(item)
        p += 1
    return primes

# task 4 #
def anagrams(word, word_list):
    sorted_word_list = list(map(lambda item: ''.join(set(item)).lower(), word_list))
    word = ''.join(set(word))
    anagramList = []
    for i in range(0, len(sorted_word_list)):
        if(sorted_word_list[i] == word):
            anagramList.append(word_list[i])
    return anagramList
    

def main():
    # task 1 #
    list1 = [1,2,3,4,5,6]
    list2 = [3,4,5,7,8,9,0]
    print(findCommonElements1(list1, list2))
    # or
    print(findCommonElements2(list1, list2))

    # task 2 #
    strings = ["rotator", "wow", "noon", "civic", "level", "Bob", "Ross", "Tenet", "a"]
    print(palindrom1(strings))
    # or
    print(palindrom2(strings))

    # task 3 #
    numList = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24,25,26,27,28,29,30]
    print(sieveOfEratosthenes(numList))

    # task 4 #
    word_list = ["enlists", "google", "inlets", "banana"]
    word = "listen"
    print(anagrams(word, word_list))

main()