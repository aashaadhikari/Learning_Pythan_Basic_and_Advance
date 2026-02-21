user_inp = int(input("Enter the num : "))

i =1
is_perfect_squaer = False

while i * i <= user_inp:
    if i*i == user_inp:
        is_perfect_squaer = True
        break
    i += 1

if is_perfect_squaer:
    print(f"{user_inp} is a perfect square.")

else:
    print(f"{user_inp} is not a perfect square.")
