from math import sqrt
from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def distance(x, y):
    dist = sqrt(x*x + y*y)
    return dist


def line_length(a, b, c, d):
    length = sqrt(((c-a)*(c-a)) + ((d-b)*(d-b)))
    return length


if line_length(x1, y1, x2, y2) >= line_length(x3, y3, x4, y4):
    if distance(x1, y1) <= distance(x2, y2):
        print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")
    else:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
else:
    if distance(x3, y3) <= distance(x4, y4):
        print(f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})")
    else:
        print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")

