def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6


def classify_triangle(a, b, c):
    if a == b and b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


def main():
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    if is_triangle(a, b, c):
        print("This is a valid triangle.")
        if is_right_triangle(a, b, c):
            print("It is also a Right Triangle.")
        print("Type:", classify_triangle(a, b, c))
    else:
        print("These sides do not form a triangle.")


if __name__ == "__main__":
    main()
