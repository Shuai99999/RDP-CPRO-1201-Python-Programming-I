Fibonacci = [0, 1]

num = int(input("Please input the iteration time: "))

for i in range(num):
    Fibonacci.append(Fibonacci[len(Fibonacci) - 2] + Fibonacci[len(Fibonacci) - 1])

print(Fibonacci)
