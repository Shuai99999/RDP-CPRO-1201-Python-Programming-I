num = int(input('Please input a number: '))

for i in range(1, num + 1):
    if num % i == 0 and i % 2 != 0: 
        print(f"{i} is one of the number's odd factors.")
