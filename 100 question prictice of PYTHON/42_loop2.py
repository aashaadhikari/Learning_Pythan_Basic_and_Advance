# write a program to count the number of vowels in the word.

vowels = "a, e, i, o, u"

user_inpo = input("Enter the word: ")

# count = 0
found_vowels = [] # to store vowels found

for chr in user_inpo.lower():
    if chr in vowels:
        # count += 1
        found_vowels.append(chr)

# remove duplicates if you only want unique vowels
unique_vowels = set(found_vowels)

print(f"Total vowels in {user_inpo} is {len(found_vowels)}")
print(f"Vowels present are: {', '.join(unique_vowels)}")