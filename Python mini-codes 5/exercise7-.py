def f(x):
    return x**3 - 6 * x**2 + 11 * x - 6


def find_roots(a, b, accuracy):
    roots = []
    step = 0.001
    x = a

    while x < b:
        if f(x) * f(x + step) < 0:
            low = x
            high = x + step
            while high - low > accuracy:
                mid = (low + high) / 2
                if f(mid) == 0:
                    roots.append(mid)
                    break
                elif f(mid) * f(low) < 0:
                    high = mid
                else:
                    low = mid
            roots.append((low + high) / 2)
        x += step

    return roots


a = float(input("Enter the starting point of the interval: "))
b = float(input("Enter the ending point of the interval: "))
accuracy = 0.0001

roots = find_roots(a, b, accuracy)
print("The roots are:", roots)
