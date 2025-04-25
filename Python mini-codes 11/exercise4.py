num = int(input("Enter a number: "))
div_sum = 0
for i in range(1, num):
    if num % i == 0:
        div_sum += i
if div_sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")
