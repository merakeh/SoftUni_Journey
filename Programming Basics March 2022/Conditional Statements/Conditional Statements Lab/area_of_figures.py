from math import pi
figure = str(input())
result = 0
if figure == "square":
    side = float(input())
    result = side * side
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
elif figure == "circle":
    radius = float(input())
    result = pi * radius**2
elif figure == "triangle":
    side_c = float(input())
    height_c = float(input())
    result = side_c * height_c / 2
print(f"{result:.3f}")
