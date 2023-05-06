guess = 'ecmndada';

print("Please enter 4 strings,\n2 of them must start with consonants,\non the other hand the remaining 2 must start with non consonants.")

ascii_noncons = 'bcdfghjklmnpqrstvwxyz'
ascii_cons = 'aeiou'
cons = 0
noncons = 0
point = 0

for i in range(4):
    string = ''
    while(True):
        string = input("Please enter "+ str(i+1) +". string: ")
        if(cons < 2 and noncons < 2):
            if(ascii_cons.__contains__(string[0])):
                cons += 1
            elif (ascii_noncons.__contains__(string[0])):
                noncons += 1
            break
        elif(cons < 2 and ascii_cons.__contains__(string[0])):
            cons += 1
            break
        elif(noncons < 2 and ascii_noncons.__contains__(string[0])):
            noncons += 1
            break
        else:
            print("Invalid input, please try again.")

    len_str = len(string)

    for j in range(len(guess)):
        if(string in guess[j: (j + len_str)]):
            point += 1
            print(point)

print("The game is over. Your point: " + str(point))
if(point >= 4):
    print("You won.")
else:
    print("You didn't win")