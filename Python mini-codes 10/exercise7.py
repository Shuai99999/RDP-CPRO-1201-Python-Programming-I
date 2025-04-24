num = int(input("Please input a number: "))
base = 2

i = num
res = ""

while i > 0:
    remainder = i % base
    i = i // base

    if remainder < 10:
        digit = str(remainder)
    else:
        digit = chr(ord("A") + remainder - 10)

    res = digit + res

print(res)
