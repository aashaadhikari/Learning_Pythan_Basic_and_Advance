# solution 1 using / operator

# dect = {"john": 89, "aasha":99}
# dect2 = {"aasha":94, "peter":78}

# print(dect | dect2)



# solution no. 2


# dect = {"john": 89, "aasha":99}
# dect2 = {"aasha":94, "peter":78}

# print({**dect, **dect2})


# solution no. 3
# used copy and update

dect = {"john": 89, "aasha":99}
dect2 = {"aasha":94, "peter":78}

dect3 = dect2.copy()
dect3.update(dect)

print(dect3)