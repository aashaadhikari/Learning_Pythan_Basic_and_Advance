# convert celsius to fahrenheit

def celsius_to_fahrenhight(x):

    fahrenhight = (x * 9/5) + 32  # formula of it
    return fahrenhight

user_input = int(input("Enter the celsius degree: "))


convert_celsius = celsius_to_fahrenhight(user_input)

print("converted once",convert_celsius)



