user_list = input("Enter a list of numbers separated by spaces: ").split()
user_list = [int(num) for num in user_list]

for i in range(len(user_list)):
    for j in range(i + 1, len(user_list)):
        if user_list[i] > user_list[j]:
            user_list[i], user_list[j] = user_list[j], user_list[i]

input_len = len(user_list)

if input_len % 2 == 0:
    medium_index = input_len / 2
    print((user_list[int(medium_index - 1)] + user_list[int(medium_index)]) / 2)
else:
    medium_index = (input_len - 1) / 2
    print(user_list[int(medium_index)])
