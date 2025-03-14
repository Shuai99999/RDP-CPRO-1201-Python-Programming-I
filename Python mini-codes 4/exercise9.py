numbers = []
print("Enter 3 numbers:")
for i in range(3):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("The numbers in descending order are:", numbers)
