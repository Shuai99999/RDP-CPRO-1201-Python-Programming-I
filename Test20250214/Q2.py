num1 = int(input('Please input the first number: '))
num2 = int(input('Please input the second number: '))

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

for i in range(num1, num2 + 1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(f"{i} is prime number")