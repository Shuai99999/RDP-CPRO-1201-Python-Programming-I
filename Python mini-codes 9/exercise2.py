unit = input("Enter temperature unit (C/F): ").strip().lower()
value = float(input("Enter the temperature value: "))

if unit == "c":
    f = int((value * 9 / 5) + 32)
    print(f"{int(value)}°C is {f} in Fahrenheit")
elif unit == "f":
    c = int((value - 32) * 5 / 9)
    print(f"{int(value)}°F is {c} in Celsius")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
