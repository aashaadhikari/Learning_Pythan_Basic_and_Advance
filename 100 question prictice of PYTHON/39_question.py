# Remove Punctuations From a String (), [], {}. _, -, "", !, <>, 

punc = '''!()-[]:"/,\<>.?@#$%^&*~'''


user_inpo = input("Enter the string:  ")

empty_str = ""

for i in user_inpo:
    if i not in punc:
        empty_str += i

print (empty_str)

