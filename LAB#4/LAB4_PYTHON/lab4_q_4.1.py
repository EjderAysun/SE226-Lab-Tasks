print("----------fourth task----------")

print("----------4.1.a----------")
# task 4.1.a
dictionary = dict()
for i in range(1, 31):
    dictionary[i] = (i - 1) * (i + 1)
print("process completed")

print("----------4.1.b----------")
# task 4.1.b
for key, value in dictionary.items():
    print("%s: %s" %(key, value))
    # i is a key from dictionary
    # dictionary[i] is the value of the i key from dictionary

print("----------4.1.c----------")
# task 4.1.c
sum = 0
for key in dictionary:
    sum += dictionary[key]
print("sum: %s" %sum)

print("----------4.1.d----------")
# task 4.1.d
# It will be assumed that the user has entered a number.
num = int(input("Please enter a value: "))
keys_to_delete = []

for key, value in dictionary.items():
    if value == num:
        keys_to_delete.append(key)

if(len(keys_to_delete) != 0):
    for key in keys_to_delete:
        del dictionary[key]
    print("Dictionary after deletion: %s" %dictionary)
else:
    print("The value you entered is not available in the dictionary.")