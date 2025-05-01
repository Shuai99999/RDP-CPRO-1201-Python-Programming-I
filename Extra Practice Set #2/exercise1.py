lst = input("Enter list elements separated by spaces: ").split()
lst = [int(x) for x in lst]
n = int(input("Enter rotation count: "))

n = n % len(lst)
rotated = lst[-n:] + lst[:-n]
print(rotated)
