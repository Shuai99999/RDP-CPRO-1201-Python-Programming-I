Fibonacci = [0, 1]

# num = int(input("Please input the iteration time: "))
num = 13
while num < 0:
    num = int(input("The iteration time should be a positive number: "))

for i in range(num):
    Fibonacci.append(Fibonacci[len(Fibonacci) - 2] + Fibonacci[len(Fibonacci) - 1])

print(Fibonacci)
