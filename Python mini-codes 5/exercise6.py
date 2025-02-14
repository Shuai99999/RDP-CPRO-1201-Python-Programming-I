def count_two_repeating_digits(start, end):
    """
    Counts numbers with exactly two repeating digits in the range [start, end].
    """
    count = 0
    for num in range(start, end + 1):
        digits = str(num)
        # Check if exactly two digits are the same
        if len(set(digits)) == 2:
            count += 1
            print(digits)
    return count


print(count_two_repeating_digits(106, 306))
