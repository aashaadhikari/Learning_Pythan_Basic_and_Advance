# POLYMORPHISM IN FUNCATION
  # In Python, polymorphism allows same method, function or operator to behave differently depending on object it is working with.



# Write a funcation multiply the multiplies two number, but can accept and multiply string.

def multiply(p1, p2):
    return p1 * p2

print(multiply(2, 5))
print(multiply('a', 5))
print(multiply(5, 'b'))
print(multiply('5', 4))
