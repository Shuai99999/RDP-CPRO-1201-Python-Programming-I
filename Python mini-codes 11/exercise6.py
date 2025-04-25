total = 0.0

while True:
    entry = input("Enter operation (e.g., + 5), or 'Enter' to finish: ").strip()
    if entry == "Enter":
        break

    parts = entry.split()
    if len(parts) != 2:
        print("Invalid input format. Use: + 5 or * 2")
        continue

    operator, value = parts[0], parts[1]
    try:
        num = float(value)
    except ValueError:
        print("Invalid number.")
        continue

    if operator == "+":
        total += num
    elif operator == "-":
        total -= num
    elif operator == "*":
        total *= num
    elif operator == "/":
        if num == 0:
            print("Error: Division by zero.")
            continue
        total /= num
    else:
        print("Invalid operator. Use +, -, *, or /.")

print("Result:", total)
