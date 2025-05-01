factorial = 1
isInt = False

while not isInt:
    num = input("Please input a positive whole number: ")
    while num < 0:
        num = int(input("The number should be positive: "))

    try:
        int(num)
        isInt = True
        num = int(num)
    except ValueError:
        print("Your input is not a whole number.")

for i in range(1, num + 1):
    factorial *= i
print(f"The {num}'s factorial is {factorial}")
