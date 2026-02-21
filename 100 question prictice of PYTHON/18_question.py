# Calculate Area of a triangle with 3 side length
# Formula:square root of  s*(s-a)*(s-b*(s-c) where s = semi_perimeter

# Use
#1. user Inputes
#2. funcation
#3. F_strings

import math
def cal_area(sidea, sideb, sidec):
    semi_perimeter = (sidea + sideb + sidec)/2
    area_sq = semi_perimeter*(semi_perimeter-sidea)*(semi_perimeter-sideb)*(semi_perimeter-sidec)
    t_area = math.sqrt(area_sq)
    #return math.sqrt(area_sq)
    return t_area

sidea = int(input("Enter length of side 1: "))
sideb = int(input("Enter length of side 2: "))
sidec = int(input("Enter length of side 3: "))

area = cal_area(sidea, sideb, sidec)
print(f"the area is {area}")