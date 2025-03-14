numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

even_numbers = [num for num in numbers if num % 2 == 0]

if even_numbers:
    print("Even numbers:", even_numbers)
else:
    print("Error: No even numbers found in the list.")
