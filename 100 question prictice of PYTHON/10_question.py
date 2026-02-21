# Find the number of word in a sentance
# example: how are you -> 3

# use:
# 1. user input
# 2. funcation
# 3. f - string   

# additional tasks : count only words

import re

def count_word(sentance):
    # word_list = sentance.split()
    word_list = re.findall(r'\b\w+\b', sentance) #only count words
    print(word_list)
    return len(word_list)

user_input = input("Please enter your sentance: ")

new_words = count_word(user_input)
print(f"the number of word in your sentance is: {new_words}")