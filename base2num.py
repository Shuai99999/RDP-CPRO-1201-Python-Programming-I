num = 49
base = 3
i = num
res = ""
while i > 0:
    remainder = i % base
    i = i // base
    res = str(remainder) + res
print(res)
