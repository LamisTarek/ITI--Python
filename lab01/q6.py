# 6 - Ask the user to enter the radius of a circle in order to alert its calculated
# area and circumference
import math

def circle(rad):
    circumference = 2 * rad * math.pi
    area = rad ** 2 * math.pi
    print("Area: ", area)
    print("Circumference: ",circumference)


rad = int(input("Enter circule radiud: "))
circle(rad)
