num = int(input("Please input a number: "))
base = 2
i = num
res = ""
while i > 0:
    remainder = i % base
    i = i // base
    res = str(remainder) + res
print(res)
