from math import sqrt
from math import floor
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def distance(x, y):
    dist = sqrt(x*x + y*y)
    return dist


if distance(x1, y1) <= distance(x2, y2):
    print(f"({floor(x1)}, {floor(y1)})")
else:
    print(f"({floor(x2)}, {floor(y2)})")

