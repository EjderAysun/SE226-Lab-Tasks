print("----------fourth task----------")

divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}

print("----------4.2.a----------")
# task 4.2.a #
united_we_stand = dict()
united_we_stand.update(we_fall)
united_we_stand.update(divided)
print("Name%sAge" %(10*" "))
for key, value in united_we_stand.items():
    gap = 14 - len(key)
    print("%s%s%s" % (key, gap*" ", value))

print("----------4.2.b----------")
# task 4.2.b #
united_we_stand_copy = united_we_stand.copy()
del united_we_stand_copy['Nat']
print("Dictionary after 'Nat' deletion: %s" %united_we_stand_copy)

print("----------4.2.c----------")
# task 4.2.c #
keys = list(united_we_stand.keys())
keys.sort()
sorted_dict = {i: united_we_stand[i] for i in keys}
print("Sorted dictionary: %s" %sorted_dict)

print("----------4.2.d----------")
# task 4.2.d #
values = list(united_we_stand.values())
min = values[0]
max = values[0]

for i in range(1, len(values)):
    num = values[i]
    if(num > max):
        max = num
    elif(num < min):
        min = num
print("Max: %s\nMin: %s" % (max, min))