input_list = input("Enter a list of numbers separated by spaces: ").split()
num_list = [int(num) for num in input_list]
sum_list = 0
for i in num_list:
    sum_list += i
average = sum_list / len(num_list)
print(average)
