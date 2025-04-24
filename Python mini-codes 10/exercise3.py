import math

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180 - angle_A - angle_B

    print("Triangle type:", triangle_type)
    print(f"Angles: A = {angle_A:.2f}°, B = {angle_B:.2f}°, C = {angle_C:.2f}°")
else:
    print("The given side lengths do not form a valid triangle.")
