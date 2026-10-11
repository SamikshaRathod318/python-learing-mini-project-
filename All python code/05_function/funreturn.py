import math


def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a,c = calculate_circle_area(2)
print("Area:", a, "Circumference:", c)  # Output: Area: 12.566370614359172 Circumference: 12.566370614359172