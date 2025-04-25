data = [
    18,
    60,
    -10,
    17,
    55,
    8,
    -1,
    31,
    52,
    31,
    27,
    14,
    25,
    0,
    -2,
    15,
    -1,
    50,
    45,
    -4,
    42,
    -10,
    40,
    3,
    43,
    55,
    24,
    -17,
    17,
    54,
    19,
    24,
    44,
    30,
    24,
    3,
    -17,
    31,
    45,
    -10,
    13,
    -12,
    21,
    -13,
    52,
    57,
    -1,
    37,
    21,
    42,
]

maximum = data[0]
minimum = data[0]
sum_of_data = 0
count = 0

for num in data:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
    sum_of_data += num
    count += 1

mean_of_data = sum_of_data / count

sum_squared_diff = 0
for num in data:
    sum_squared_diff += (num - mean_of_data) ** 2

standard_deviation = (sum_squared_diff / count) ** 0.5

print("Without built-in functions:")
print("maximum =", maximum)
print("minimum =", minimum)
print("sum_of_data =", sum_of_data)
print("mean_of_data =", mean_of_data)
print("standard_deviation =", standard_deviation)
