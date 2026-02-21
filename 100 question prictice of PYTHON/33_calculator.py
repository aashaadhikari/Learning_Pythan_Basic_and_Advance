

print("****** Mini calcularor ********")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("press 1 for addition \n press 2 for subtraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("Your choice from your solution: "))

if choice == 1:
    print(num1 + num2)

elif choice == 2:
    print(num1-num2)

elif choice == 2:
    print(num1 * num2)

else:
    print(num1 % num2)