numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

max_num = numbers[0]

for i in numbers:
    if i > max_num:
        max_num = i

print(f"The maximum number in the list is: {max_num}")
