#  Sort Words in Alphabetic Order

a = "HarrY Potter and the Goblet of Fire"
# user_inpo = input("Enter the string: ")

w = a.split()

print(w)

for i in range(len(w)):
    w[i] = w[i].lower()


print(w)

w.sort()
print(w)

 