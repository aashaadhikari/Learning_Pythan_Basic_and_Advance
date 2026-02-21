# write a python program to count accurrences of each character in the word "programming.


word ="programming"

char_count = {}

for char in word:
    if char in char_count:
        char_count[char] += 1

    else:
        char_count[char] = 1


for char, count in char_count.items():
    print(char +':', count)