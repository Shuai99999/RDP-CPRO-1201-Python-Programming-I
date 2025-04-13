def classify_triangle(a, b, c):
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


def triangle_classifier():
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))

    if a + b > c and a + c > b and b + c > a:
        result = classify_triangle(a, b, c)
        print("The triangle is:", result)
    else:
        print("Not a valid triangle.")


triangle_classifier()
