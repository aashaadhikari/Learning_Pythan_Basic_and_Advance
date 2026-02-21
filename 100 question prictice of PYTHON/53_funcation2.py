# FUNCATION RETURN MULTIPLE VALUES

# Create a funcation the return both the area and circumference of a circle given its radius.
import math
def circle_stats(radius):
    area= math.pi*radius ** 2
    circumference= 2* math.pi*radius
    return area, circumference

a, c = circle_stats(3)
print(f"Area {a:0,.2f} circumference {c:0,.2f}")
