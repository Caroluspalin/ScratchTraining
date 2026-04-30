def is_valid(sides):
    a, b, c = sides[0], sides[1], sides[2]
    return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    a, b, c = sides[0],sides[1], sides[2]
    same = a == b and b==c
    return is_valid(sides) and same


def isosceles(sides):
    a, b, c = sides[0], sides[1], sides[2]
    same = a == b or a == c or b == c
    return is_valid(sides) and same


def scalene(sides):
    a, b, c = sides[0], sides[1], sides[2]
    different = a != b and b != c and a != c
    return is_valid(sides) and different

print(scalene([2,3,3]))