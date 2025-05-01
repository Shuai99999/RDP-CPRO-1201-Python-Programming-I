input_list = input("Enter a list of numbers separated by spaces: ").split()

num_list = [int(num) for num in input_list]


def find_least_difference(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    if len(numbers) < 2:
        return "Not enough elements to compare."

    min_diff = float("inf")

    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff

    return min_diff


least_difference = find_least_difference(num_list)

print(f"Least difference between elements: {least_difference}")
