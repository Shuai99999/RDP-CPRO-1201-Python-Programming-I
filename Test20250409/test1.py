coins = int(input("Please input the coins number: "))
total = float(input("Please input the total value: "))
isFound = False

for i in range(coins + 1):
    for j in range(coins + 1 - i):
        if i + j == coins and 1 * i + 0.25 * j == total:
            isFound = True
            print(f"Number of Loonies: {i}, Number of Quarters: {j}")
            break
    else:
        continue

if not isFound:
    print("No applicable scenarios.")
