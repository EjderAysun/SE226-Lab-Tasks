from abc import (
  ABC,
  abstractmethod,
)

# task 1 #
class address(ABC):
    def __init__(self, address):
        self.address = address;

    @abstractmethod
    def calculateFreqs(self):
        pass

# task 2 #
class ListCount(address):
    # task 3 #
    def calculateFreqs(self):
        with open(self.address, 'r') as f:
            text = f.read().lower()
        unique_letters = set(text)
        frequencies_list = []
        for char in unique_letters:
            if char.isalpha():
                count = text.count(char)
                frequencies_list.append('%s: %s' %(char, count))
        print(frequencies_list)


class DictCount(address):
    # task 4 #
    def calculateFreqs(self):
        with open(self.address, 'r') as f:
            text = f.read().lower()
        unique_letters = set(text)
        frequencies_dictionary = dict()
        for char in unique_letters:
            if char.isalpha():
                frequencies_dictionary.__setitem__(char, 0)
        for char in text:
            if char in frequencies_dictionary:
                frequencies_dictionary[char] += 1
        print(frequencies_dictionary)

# task 5 #
list_counter = ListCount('Mission_Documents#8/weirdWords.txt')
list_counter.calculateFreqs()
print("-----------------------------------------------------")
dict_counter = DictCount('Mission_Documents#8/weirdWords.txt')
dict_counter.calculateFreqs()