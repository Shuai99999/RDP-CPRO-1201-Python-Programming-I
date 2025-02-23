input_list = input("Enter a list of numbers separated by spaces: ").split()

num_list = [int(num) for num in input_list]


def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    return round(total / count, 2)


def calculate_median(numbers):
    numbers = sorted(numbers)
    length = 0
    for _ in numbers:
        length += 1
    mid = length // 2

    if length % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:  # Odd length
        return round(numbers[mid], 2)


def calculate_mode(numbers):
    freq_dict = {}
    for num in numbers:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    max_count = 0
    mode = None
    for key, value in freq_dict.items():
        if value > max_count:
            max_count = value
            mode = key
        elif value == max_count:
            mode = "No unique mode"

    return mode


def calculate_range(numbers):
    min_value = numbers[0]
    max_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return round(max_value - min_value, 2)


def calculate_standard_deviation(numbers):
    mean = calculate_average(numbers)
    variance_sum = 0
    count = 0

    for num in numbers:
        variance_sum += (num - mean) ** 2
        count += 1

    variance = variance_sum / (count - 1)
    return round(variance**0.5, 2)


# Calculate statistics manually
average = calculate_average(num_list)
median = calculate_median(num_list)
mode = calculate_mode(num_list)
range_value = calculate_range(num_list)
std_dev = calculate_standard_deviation(num_list)

# Display results
print(f"Average: {average}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Range: {range_value}")
print(f"Standard Deviation: {std_dev}")
