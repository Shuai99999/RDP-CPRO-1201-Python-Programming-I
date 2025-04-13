while True:
    user_input = input("Enter a float number: ")
    try:
        num = float(user_input)
        break
    except ValueError:
        print("Invalid input. Please enter a valid float.")

if num < 0:
    num = -num

print(f"The absolute value is: {num}")
