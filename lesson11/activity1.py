string1 = input("Enter your word")

char1 = input("Enter your character")

i = 0
count = 0

while i < len(string1) :
    if string1[i] == char1:
        count += 1
        i += 1

    print(" The total Number of Times ", char1, " has Occured = ", count)    