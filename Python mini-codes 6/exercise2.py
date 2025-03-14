def collatz_conjecture(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)  # Print each step to visualize the process
        steps += 1
    print(f"Total steps taken: {steps}")


number = int(input("Enter a number to apply the Collatz conjecture: "))
collatz_conjecture(number)
