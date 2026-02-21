# let's save given list is: [1,2,3,4,5,6,7,8,9]
# The output should be: [2,4,6,8] even num

# Use:
# List comprehesion 
# F_string

number = [10,11,12,13,14,15,16,17,18,19]
filter_list = [num for num in number if num%2 == 0]
print (f"filtered list is {filter_list}")