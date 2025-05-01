input_list = input("Enter a list of numbers separated by spaces: ").split()

num_list = [int(num) for num in input_list]

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        if num_list[i] > num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

print("Sorted list in ascending order:", num_list)
