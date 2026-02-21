# Caalculate Binary to Decimal
# Example: 1011 = 1+2+0+8 = 11

# use:
# 1. Funcation
# 2. Tuple Assignment

def con_binary(binary):
    revrse_binary = binary[::-1]
    decimal = 0
    for i in range(len(revrse_binary)):
        two_powered = (2**i) * int(revrse_binary[i])
        decimal = decimal + int(two_powered)

    return decimal


binary = '1011'
decimal = con_binary(binary)
print(f" {binary} to decimal is {decimal}")