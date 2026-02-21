
# FUNCATION WITH **kwargs

# Create a funcation that accept any number of keyword argument and print them in the format.
#key:value


# def print_kwargs(name, power):
 # print("Name:", name, "Power:", power)
def print_kwargs(**kwrgs):
    for key, value in kwrgs.items():
        print(f"{key}: {value}")
    

print_kwargs(name="aasha", power="lazer")
print_kwargs(employed="Dr.ranita")
