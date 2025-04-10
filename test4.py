def nearest_perfect_squares(n):
    # Find the largest perfect square smaller than n
    smaller = n - 1
    while True:
        root = 1
        while root * root <= smaller:
            if root * root == smaller:
                break
            root += 1
        if root * root == smaller:
            break
        smaller -= 1

    # Find the smallest perfect square larger than n
    larger = n + 1
    while True:
        root = 1
        while root * root <= larger:
            if root * root == larger:
                break
            root += 1
        if root * root == larger:
            break
        larger += 1

    return smaller, larger


# Example usage
number = 50
smaller_square, larger_square = nearest_perfect_squares(number)
print(f"Nearest smaller perfect square: {smaller_square}")
print(f"Nearest larger perfect square: {larger_square}")
