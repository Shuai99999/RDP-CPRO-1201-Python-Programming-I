import math


def calculate_nPr(n, r):
    return math.perm(n, r)


def calculate_nCr(n, r):
    return math.comb(n, r)


n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

nPr = calculate_nPr(n, r)
nCr = calculate_nCr(n, r)

print(f"The value of {n}P{r} (permutations) is: {nPr}")
print(f"The value of {n}C{r} (combinations) is: {nCr}")
