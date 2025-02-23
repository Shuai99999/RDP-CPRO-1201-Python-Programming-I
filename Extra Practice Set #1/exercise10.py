# Taking a list of numbers as input from the user
input_list = input("Enter a list of numbers separated by spaces: ").split()

# Convert the input strings to integers
num_list = [int(num) for num in input_list]

# Sorting the list in descending order
for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        if num_list[i] > num_list[j]:
            # Swap the elements if they are in the wrong order
            num_list[i], num_list[j] = num_list[j], num_list[i]

# Printing the sorted list in descending order
print("Sorted list in descending order:", num_list)
